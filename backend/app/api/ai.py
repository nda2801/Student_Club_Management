import json
from flask import Blueprint, request, jsonify, g
from pydantic import ValidationError
from app.core.security import jwt_required, roles_required
from app.models.models import Task, User, AILog
from app.schemas.schemas import AIAnnouncementRequest, AISummaryRequest, AIAssignmentRequest
from app.services.ai_service import AIService

router = Blueprint("ai", __name__)

@router.route("/generate-announcement", methods=["POST"])
@jwt_required
def generate_announcement():
    data = request.get_json()
    if not data:
        return jsonify({"detail": "Thiếu dữ liệu yêu cầu sinh thông báo"}), 400
        
    try:
        req = AIAnnouncementRequest.model_validate(data)
    except ValidationError as e:
        return jsonify({"detail": e.errors()}), 422
        
    db = g.db
    current_user = g.current_user
    
    announcement = AIService.generate_announcement(
        activity_title=req.activity_title,
        activity_description=req.activity_description,
        start_time=req.start_time,
        location=req.location,
        tone=req.tone or "enthusiastic"
    )
    
    log = AILog(
        user_id=current_user.id,
        prompt_type="ANNOUNCEMENT",
        input_data=json.dumps(req.model_dump()),
        output_result=announcement
    )
    db.add(log)
    db.commit()
    
    return jsonify({"result": announcement}), 200

@router.route("/summarize-activity", methods=["POST"])
@jwt_required
def summarize_activity():
    data = request.get_json()
    if not data:
        return jsonify({"detail": "Thiếu dữ liệu yêu cầu tóm tắt"}), 400
        
    try:
        req = AISummaryRequest.model_validate(data)
    except ValidationError as e:
        return jsonify({"detail": e.errors()}), 422
        
    db = g.db
    current_user = g.current_user
    
    summary = AIService.summarize_activity(
        activity_title=req.activity_title,
        meeting_notes=req.meeting_notes,
        member_feedbacks=req.member_feedbacks or []
    )
    
    log = AILog(
        user_id=current_user.id,
        prompt_type="SUMMARY",
        input_data=json.dumps(req.model_dump()),
        output_result=summary
    )
    db.add(log)
    db.commit()
    
    return jsonify({"result": summary}), 200

@router.route("/suggest-assignments", methods=["POST"])
@jwt_required
def suggest_assignments():
    data = request.get_json()
    if not data:
        return jsonify({"detail": "Thiếu dữ liệu yêu cầu phân công"}), 400
        
    try:
        req = AIAssignmentRequest.model_validate(data)
    except ValidationError as e:
        return jsonify({"detail": e.errors()}), 422
        
    db = g.db
    current_user = g.current_user
    
    tasks = db.query(Task).filter(Task.id.in_(req.task_ids)).all()
    if not tasks:
        return jsonify({"detail": "Không tìm thấy danh sách nhiệm vụ"}), 404
        
    members = db.query(User).all()
    
    tasks_data = []
    for t in tasks:
        tasks_data.append({
            "id": t.id,
            "title": t.title,
            "required_skill": t.required_skill
        })
        
    members_data = []
    for m in members:
        skills = json.loads(m.skills) if m.skills else []
        free_slots = json.loads(m.free_slots) if m.free_slots else []
        dept_name = m.department.name if m.department else ""
        members_data.append({
            "id": m.id,
            "full_name": m.full_name,
            "skills": skills,
            "free_slots": free_slots,
            "department_name": dept_name
        })
        
    suggestions = AIService.suggest_assignments(tasks_data, members_data)
    
    log = AILog(
        user_id=current_user.id,
        prompt_type="RECOMMEND",
        input_data=json.dumps(req.model_dump()),
        output_result=json.dumps(suggestions)
    )
    db.add(log)
    db.commit()
    
    return jsonify({"suggestions": suggestions}), 200
