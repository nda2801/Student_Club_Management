import hashlib
import json
import math
from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify, g
from pydantic import ValidationError
from jose import jwt, JWTError
from app.core.config import settings
from app.core.security import jwt_required, roles_required
from app.models.models import Activity, Attendance, User
from app.schemas.schemas import ActivityCreate, AttendanceCheckin

router = Blueprint("activities", __name__)

def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate distance in meters between two GPS points using Haversine formula."""
    R = 6371000 # Earth radius in meters
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2.0)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def generate_user_qr_token(user_id: int, activity_id: int, end_time: datetime) -> str:
    """Generate a dynamic, person-specific signed QR token valid until activity end_time."""
    exp = end_time if end_time else datetime.utcnow() + timedelta(hours=4)
    payload = {
        "sub": str(user_id),
        "act_id": activity_id,
        "exp": exp,
        "iat": datetime.utcnow(),
        "type": "DYNAMIC_PERSONAL_QR"
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

@router.route("", methods=["GET"])
@jwt_required
def get_activities():
    db = g.db
    activities = db.query(Activity).order_by(Activity.start_time.desc()).all()
    results = []
    for act in activities:
        att_count = db.query(Attendance).filter(Attendance.activity_id == act.id).count()
        results.append({
            "id": act.id,
            "title": act.title,
            "description": act.description,
            "start_time": act.start_time.isoformat() if act.start_time else None,
            "end_time": act.end_time.isoformat() if act.end_time else None,
            "location": act.location,
            "latitude": act.latitude,
            "longitude": act.longitude,
            "radius_meters": act.radius_meters,
            "status": act.status,
            "qr_code_hash": act.qr_code_hash,
            "created_by": act.created_by,
            "attendance_count": att_count
        })
    return jsonify(results), 200

@router.route("", methods=["POST"])
@jwt_required
@roles_required("ADMIN", "LEADER")
def create_activity():
    data = request.get_json()
    if not data:
        return jsonify({"detail": "Dữ liệu sự kiện không hợp lệ"}), 400
        
    try:
        act_in = ActivityCreate.model_validate(data)
    except ValidationError as e:
        return jsonify({"detail": e.errors()}), 422
        
    db = g.db
    current_user = g.current_user
    
    end_dt = act_in.end_time or (act_in.start_time + timedelta(hours=3))
    hash_str = f"ACT_{datetime.utcnow().timestamp()}_{act_in.title}"
    qr_hash = hashlib.md5(hash_str.encode('utf-8')).hexdigest()[:12]
    
    act = Activity(
        title=act_in.title,
        description=act_in.description,
        start_time=act_in.start_time,
        end_time=end_dt,
        location=act_in.location,
        latitude=act_in.latitude or 21.028511,
        longitude=act_in.longitude or 105.804817,
        radius_meters=act_in.radius_meters or 100.0,
        status=act_in.status or "UPCOMING",
        qr_code_hash=qr_hash,
        created_by=current_user.id
    )
    db.add(act)
    db.commit()
    db.refresh(act)
    
    return jsonify({
        "id": act.id,
        "title": act.title,
        "description": act.description,
        "start_time": act.start_time.isoformat() if act.start_time else None,
        "end_time": act.end_time.isoformat() if act.end_time else None,
        "location": act.location,
        "latitude": act.latitude,
        "longitude": act.longitude,
        "radius_meters": act.radius_meters,
        "status": act.status,
        "qr_code_hash": act.qr_code_hash,
        "created_by": act.created_by,
        "attendance_count": 0
    }), 201

@router.route("/<int:activity_id>/my-qr", methods=["GET"])
@jwt_required
def get_my_activity_qr(activity_id: int):
    """Generate or retrieve unique dynamic QR token for current member."""
    db = g.db
    current_user = g.current_user
    
    act = db.query(Activity).filter(Activity.id == activity_id).first()
    if not act:
        return jsonify({"detail": "Không tìm thấy sự kiện"}), 404
        
    qr_token = generate_user_qr_token(current_user.id, act.id, act.end_time)
    
    return jsonify({
        "activity_id": act.id,
        "activity_title": act.title,
        "user_id": current_user.id,
        "user_name": current_user.full_name,
        "qr_token": qr_token,
        "expires_at": act.end_time.isoformat() if act.end_time else None
    }), 200

@router.route("/checkin", methods=["POST"])
@jwt_required
def checkin_activity():
    """Anti-Proxy QR Checkin Endpoint."""
    data = request.get_json()
    if not data:
        return jsonify({"detail": "Dữ liệu điểm danh không hợp lệ"}), 400
        
    try:
        checkin_in = AttendanceCheckin.model_validate(data)
    except ValidationError as e:
        return jsonify({"detail": e.errors()}), 422
        
    db = g.db
    current_user = g.current_user
    
    act = db.query(Activity).filter(Activity.id == checkin_in.activity_id).first()
    if not act:
        return jsonify({"detail": "Không tìm thấy sự kiện cần điểm danh"}), 404
        
    # Check if user passed a dynamic QR Token
    target_user_id = current_user.id
    if checkin_in.qr_code_hash and len(checkin_in.qr_code_hash) > 30:
        try:
            payload = jwt.decode(checkin_in.qr_code_hash, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            if payload.get("type") == "DYNAMIC_PERSONAL_QR":
                if payload.get("act_id") != act.id:
                    return jsonify({"detail": "Mã QR này không khớp với sự kiện hiện tại"}), 400
                if current_user.role in ["ADMIN", "LEADER"]:
                    target_user_id = int(payload.get("sub"))
        except JWTError:
            pass
            
    # Check duplicate checkin
    existing = db.query(Attendance).filter(
        Attendance.activity_id == act.id,
        Attendance.user_id == target_user_id
    ).first()
    if existing:
        return jsonify({"detail": "Bạn (hoặc thành viên này) đã được điểm danh sự kiện này rồi!"}), 400
        
    # Geofence check
    if checkin_in.user_lat is not None and checkin_in.user_lng is not None and act.latitude and act.longitude:
        distance = haversine_distance(checkin_in.user_lat, checkin_in.user_lng, act.latitude, act.longitude)
        allowed_radius = (act.radius_meters or 100.0) + 150.0 # 150m GPS buffer
        if distance > allowed_radius:
            return jsonify({
                "detail": f"Vị trí điểm danh ngoài phạm vi cho phép ({int(distance)}m > {int(allowed_radius)}m). Vui lòng đến gần hội trường sự kiện."
            }), 400
            
    att = Attendance(
        activity_id=act.id,
        user_id=target_user_id,
        checkin_time=datetime.utcnow(),
        status="PRESENT",
        device_fingerprint=checkin_in.device_fingerprint
    )
    db.add(att)
    db.commit()
    db.refresh(att)
    
    target_user = db.query(User).filter(User.id == target_user_id).first()
    return jsonify({
        "id": att.id,
        "activity_id": att.activity_id,
        "user_id": att.user_id,
        "user_name": target_user.full_name if target_user else "",
        "checkin_time": att.checkin_time.isoformat(),
        "status": att.status
    }), 201

@router.route("/<int:activity_id>/attendances", methods=["GET"])
@jwt_required
def get_activity_attendances(activity_id: int):
    db = g.db
    attendances = db.query(Attendance).filter(Attendance.activity_id == activity_id).all()
    results = []
    for a in attendances:
        results.append({
            "id": a.id,
            "activity_id": a.activity_id,
            "user_id": a.user_id,
            "user_name": a.user.full_name if a.user else "",
            "checkin_time": a.checkin_time.isoformat() if a.checkin_time else None,
            "status": a.status
        })
    return jsonify(results), 200
