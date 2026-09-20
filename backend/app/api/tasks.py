from datetime import datetime
from flask import Blueprint, request, jsonify, g
from pydantic import ValidationError
from app.core.security import jwt_required, roles_required
from app.models.models import Task, TaskAssignment, User
from app.schemas.schemas import TaskCreate, TaskStatusUpdate, TaskAssignmentCreate

router = Blueprint("tasks", __name__)

@router.route("", methods=["GET"])
@jwt_required
def get_tasks():
    db = g.db
    activity_id = request.args.get("activity_id", type=int)
    
    query = db.query(Task)
    if activity_id:
        query = query.filter(Task.activity_id == activity_id)
    tasks = query.all()
    
    results = []
    for t in tasks:
        assignment = db.query(TaskAssignment).filter(TaskAssignment.task_id == t.id).first()
        assigned_user_id = assignment.user_id if assignment else None
        assigned_user_name = assignment.user.full_name if assignment and assignment.user else None
        ai_suggested = assignment.ai_suggested if assignment else False
        match_score = assignment.match_score if assignment else 1.0
        
        results.append({
            "id": t.id,
            "activity_id": t.activity_id,
            "title": t.title,
            "description": t.description,
            "required_skill": t.required_skill,
            "deadline": t.deadline.isoformat() if t.deadline else None,
            "status": t.status,
            "assigned_user_id": assigned_user_id,
            "assigned_user_name": assigned_user_name,
            "ai_suggested": ai_suggested,
            "match_score": match_score
        })
    return jsonify(results), 200

@router.route("", methods=["POST"])
@jwt_required
@roles_required("ADMIN", "LEADER")
def create_task():
    data = request.get_json()
    if not data:
        return jsonify({"detail": "Dữ liệu nhiệm vụ không hợp lệ"}), 400
        
    try:
        task_in = TaskCreate.model_validate(data)
    except ValidationError as e:
        return jsonify({"detail": e.errors()}), 422
        
    db = g.db
    task = Task(
        activity_id=task_in.activity_id,
        title=task_in.title,
        description=task_in.description,
        required_skill=task_in.required_skill,
        deadline=task_in.deadline,
        status=task_in.status or "TO_DO"
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    
    return jsonify({
        "id": task.id,
        "activity_id": task.activity_id,
        "title": task.title,
        "description": task.description,
        "required_skill": task.required_skill,
        "deadline": task.deadline.isoformat() if task.deadline else None,
        "status": task.status
    }), 201

@router.route("/<int:task_id>/status", methods=["PUT"])
@jwt_required
def update_task_status(task_id: int):
    db = g.db
    current_user = g.current_user
    
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return jsonify({"detail": "Không tìm thấy nhiệm vụ"}), 404
        
    assignment = db.query(TaskAssignment).filter(TaskAssignment.task_id == task.id).first()
    assigned_user_id = assignment.user_id if assignment else None
    
    # RBAC Enforcement: ADMIN/LEADER can update any task; MEMBER can only update their OWN assigned task
    if current_user.role == "MEMBER":
        if not assigned_user_id or assigned_user_id != current_user.id:
            return jsonify({"detail": "Thành viên chỉ có quyền cập nhật trạng thái nhiệm vụ do chính mình phụ trách"}), 403
            
    data = request.get_json()
    if not data:
        return jsonify({"detail": "Thiếu thông tin trạng thái cần cập nhật"}), 400
        
    try:
        status_in = TaskStatusUpdate.model_validate(data)
    except ValidationError as e:
        return jsonify({"detail": e.errors()}), 422
        
    task.status = status_in.status
    db.commit()
    db.refresh(task)
    
    return jsonify({
        "id": task.id,
        "activity_id": task.activity_id,
        "title": task.title,
        "description": task.description,
        "required_skill": task.required_skill,
        "deadline": task.deadline.isoformat() if task.deadline else None,
        "status": task.status,
        "assigned_user_id": assigned_user_id,
        "assigned_user_name": assignment.user.full_name if assignment and assignment.user else None,
        "ai_suggested": assignment.ai_suggested if assignment else False,
        "match_score": assignment.match_score if assignment else 1.0
    }), 200

@router.route("/assign", methods=["POST"])
@jwt_required
@roles_required("ADMIN", "LEADER")
def assign_task():
    data = request.get_json()
    if not data:
        return jsonify({"detail": "Dữ liệu phân công không hợp lệ"}), 400
        
    try:
        assign_in = TaskAssignmentCreate.model_validate(data)
    except ValidationError as e:
        return jsonify({"detail": e.errors()}), 422
        
    db = g.db
    current_user = g.current_user
    
    task = db.query(Task).filter(Task.id == assign_in.task_id).first()
    if not task:
        return jsonify({"detail": "Không tìm thấy nhiệm vụ"}), 404
        
    user = db.query(User).filter(User.id == assign_in.user_id).first()
    if not user:
        return jsonify({"detail": "Không tìm thấy thành viên để gán việc"}), 404
        
    # Remove existing assignment if any
    db.query(TaskAssignment).filter(TaskAssignment.task_id == task.id).delete()
    
    assignment = TaskAssignment(
        task_id=task.id,
        user_id=user.id,
        ai_suggested=assign_in.ai_suggested or False,
        match_score=assign_in.match_score or 1.0,
        assigned_by=current_user.id,
        assigned_at=datetime.utcnow()
    )
    db.add(assignment)
    db.commit()
    db.refresh(assignment)
    
    return jsonify({
        "id": task.id,
        "activity_id": task.activity_id,
        "title": task.title,
        "description": task.description,
        "required_skill": task.required_skill,
        "deadline": task.deadline.isoformat() if task.deadline else None,
        "status": task.status,
        "assigned_user_id": user.id,
        "assigned_user_name": user.full_name,
        "ai_suggested": assignment.ai_suggested,
        "match_score": assignment.match_score
    }), 200
