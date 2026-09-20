import json
from flask import Blueprint, request, jsonify, g
from pydantic import ValidationError
from app.core.security import jwt_required
from app.models.models import User
from app.schemas.schemas import UserUpdate

router = Blueprint("members", __name__)

@router.route("", methods=["GET"])
@jwt_required
def get_members():
    db = g.db
    users = db.query(User).all()
    results = []
    for u in users:
        dept_name = u.department.name if u.department else "Chưa xếp ban"
        skills = json.loads(u.skills) if u.skills else []
        free_slots = json.loads(u.free_slots) if u.free_slots else []
        results.append({
            "id": u.id,
            "full_name": u.full_name,
            "email": u.email,
            "role": u.role,
            "department_id": u.department_id,
            "department_name": dept_name,
            "skills": skills,
            "free_slots": free_slots,
            "avatar_url": u.avatar_url,
            "created_at": u.created_at.isoformat() if u.created_at else None
        })
    return jsonify(results), 200

@router.route("/<int:member_id>", methods=["GET"])
@jwt_required
def get_member(member_id: int):
    db = g.db
    u = db.query(User).filter(User.id == member_id).first()
    if not u:
        return jsonify({"detail": "Không tìm thấy thành viên"}), 404
        
    dept_name = u.department.name if u.department else "Chưa xếp ban"
    skills = json.loads(u.skills) if u.skills else []
    free_slots = json.loads(u.free_slots) if u.free_slots else []
    
    return jsonify({
        "id": u.id,
        "full_name": u.full_name,
        "email": u.email,
        "role": u.role,
        "department_id": u.department_id,
        "department_name": dept_name,
        "skills": skills,
        "free_slots": free_slots,
        "avatar_url": u.avatar_url,
        "created_at": u.created_at.isoformat() if u.created_at else None
    }), 200

@router.route("/<int:member_id>", methods=["PUT"])
@jwt_required
def update_member(member_id: int):
    db = g.db
    current_user = g.current_user
    
    u = db.query(User).filter(User.id == member_id).first()
    if not u:
        return jsonify({"detail": "Không tìm thấy thành viên"}), 404
        
    # RBAC: ADMIN/LEADER or updating self
    if current_user.role not in ["ADMIN", "LEADER"] and current_user.id != member_id:
        return jsonify({"detail": "Không có quyền chỉnh sửa tài khoản này"}), 403
        
    data = request.get_json()
    if not data:
        return jsonify({"detail": "Dữ liệu cập nhật không hợp lệ"}), 400
        
    try:
        user_update = UserUpdate.model_validate(data)
    except ValidationError as e:
        return jsonify({"detail": e.errors()}), 422
        
    if user_update.full_name is not None:
        u.full_name = user_update.full_name
    if user_update.role is not None and current_user.role in ["ADMIN", "LEADER"]:
        u.role = user_update.role
    if user_update.department_id is not None:
        u.department_id = user_update.department_id
    if user_update.skills is not None:
        u.skills = json.dumps(user_update.skills)
    if user_update.free_slots is not None:
        u.free_slots = json.dumps(user_update.free_slots)
        
    db.commit()
    db.refresh(u)
    
    dept_name = u.department.name if u.department else "Chưa xếp ban"
    skills = json.loads(u.skills) if u.skills else []
    free_slots = json.loads(u.free_slots) if u.free_slots else []
    
    return jsonify({
        "id": u.id,
        "full_name": u.full_name,
        "email": u.email,
        "role": u.role,
        "department_id": u.department_id,
        "department_name": dept_name,
        "skills": skills,
        "free_slots": free_slots,
        "avatar_url": u.avatar_url,
        "created_at": u.created_at.isoformat() if u.created_at else None
    }), 200
