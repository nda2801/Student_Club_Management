from flask import Blueprint, request, jsonify, g
from pydantic import ValidationError
from app.core.security import jwt_required, roles_required
from app.models.models import Department, User
from app.schemas.schemas import DepartmentCreate

router = Blueprint("departments", __name__)

@router.route("", methods=["GET"])
@jwt_required
def get_departments():
    db = g.db
    depts = db.query(Department).all()
    results = []
    for d in depts:
        member_count = db.query(User).filter(User.department_id == d.id).count()
        results.append({
            "id": d.id,
            "name": d.name,
            "description": d.description,
            "member_count": member_count
        })
    return jsonify(results), 200

@router.route("", methods=["POST"])
@jwt_required
@roles_required("ADMIN", "LEADER")
def create_department():
    data = request.get_json()
    if not data:
        return jsonify({"detail": "Dữ liệu ban chuyên môn không hợp lệ"}), 400
        
    try:
        dept_in = DepartmentCreate.model_validate(data)
    except ValidationError as e:
        return jsonify({"detail": e.errors()}), 422
        
    db = g.db
    dept = Department(name=dept_in.name, description=dept_in.description)
    db.add(dept)
    db.commit()
    db.refresh(dept)
    
    return jsonify({
        "id": dept.id,
        "name": dept.name,
        "description": dept.description,
        "member_count": 0
    }), 201
