import json
from flask import Blueprint, request, jsonify, g
from pydantic import ValidationError
from app.core.database import SessionLocal
from app.core.security import verify_password, get_password_hash, create_access_token, jwt_required
from app.models.models import User
from app.schemas.schemas import UserCreate, UserOut

router = Blueprint("auth", __name__)

@router.route("/login", methods=["POST"])
def login():
    """Login with Email and Password, returns JWT access token."""
    username = None
    password = None
    
    # Support both JSON payload and x-www-form-urlencoded
    if request.is_json:
        data = request.get_json() or {}
        username = data.get("username") or data.get("email")
        password = data.get("password")
    else:
        username = request.form.get("username") or request.form.get("email")
        password = request.form.get("password")
        
    if not username or not password:
        return jsonify({"detail": "Vui lòng nhập đầy đủ Email và Mật khẩu"}), 400
        
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.email == username).first()
        if not user or not verify_password(password, user.password_hash):
            return jsonify({"detail": "Mật khẩu hoặc Email không chính xác"}), 401
            
        access_token = create_access_token(subject=user.id)
        
        dept_name = user.department.name if user.department else "Chưa xếp ban"
        skills = json.loads(user.skills) if user.skills else []
        free_slots = json.loads(user.free_slots) if user.free_slots else []
        
        user_out = {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "role": user.role,
            "department_id": user.department_id,
            "department_name": dept_name,
            "skills": skills,
            "free_slots": free_slots,
            "avatar_url": user.avatar_url,
            "created_at": user.created_at.isoformat() if user.created_at else None
        }
        return jsonify({
            "access_token": access_token,
            "token_type": "bearer",
            "user": user_out
        }), 200
    finally:
        db.close()

@router.route("/register", methods=["POST"])
def register():
    """Register a new member account."""
    data = request.get_json()
    if not data:
        return jsonify({"detail": "Dữ liệu đăng ký không hợp lệ"}), 400
        
    try:
        user_in = UserCreate.model_validate(data)
    except ValidationError as e:
        return jsonify({"detail": e.errors()}), 422
        
    db = SessionLocal()
    try:
        db_user = db.query(User).filter(User.email == user_in.email).first()
        if db_user:
            return jsonify({"detail": "Email này đã được đăng ký trong hệ thống"}), 400
            
        user = User(
            full_name=user_in.full_name,
            email=user_in.email,
            password_hash=get_password_hash(user_in.password),
            role=user_in.role or "MEMBER",
            department_id=user_in.department_id,
            skills=json.dumps(user_in.skills or []),
            free_slots=json.dumps(user_in.free_slots or [])
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        
        dept_name = user.department.name if user.department else "Chưa xếp ban"
        return jsonify({
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "role": user.role,
            "department_id": user.department_id,
            "department_name": dept_name,
            "skills": user_in.skills or [],
            "free_slots": user_in.free_slots or [],
            "avatar_url": user.avatar_url,
            "created_at": user.created_at.isoformat() if user.created_at else None
        }), 201
    finally:
        db.close()

@router.route("/me", methods=["GET"])
@jwt_required
def get_me():
    """Get current authenticated user info."""
    current_user = g.current_user
    dept_name = current_user.department.name if current_user.department else "Chưa xếp ban"
    skills = json.loads(current_user.skills) if current_user.skills else []
    free_slots = json.loads(current_user.free_slots) if current_user.free_slots else []
    
    return jsonify({
        "id": current_user.id,
        "full_name": current_user.full_name,
        "email": current_user.email,
        "role": current_user.role,
        "department_id": current_user.department_id,
        "department_name": dept_name,
        "skills": skills,
        "free_slots": free_slots,
        "avatar_url": current_user.avatar_url,
        "created_at": current_user.created_at.isoformat() if current_user.created_at else None
    }), 200
