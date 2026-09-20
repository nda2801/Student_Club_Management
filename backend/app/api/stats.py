from flask import Blueprint, jsonify, g
from app.core.security import jwt_required
from app.models.models import User, Department, Activity, Attendance, Task, TaskAssignment

router = Blueprint("stats", __name__)

@router.route("/dashboard", methods=["GET"])
@jwt_required
def get_dashboard_stats():
    db = g.db
    total_members = db.query(User).count()
    total_departments = db.query(Department).count()
    total_activities = db.query(Activity).count()
    total_tasks = db.query(Task).count()
    completed_tasks = db.query(Task).filter(Task.status == "DONE").count()
    total_attendances = db.query(Attendance).filter(Attendance.status == "PRESENT").count()
    
    return jsonify({
        "total_members": total_members,
        "total_departments": total_departments,
        "total_activities": total_activities,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "total_attendances": total_attendances
    }), 200

@router.route("/leaderboard", methods=["GET"])
@jwt_required
def get_leaderboard():
    db = g.db
    members = db.query(User).all()
    results = []
    
    for m in members:
        att_count = db.query(Attendance).filter(
            Attendance.user_id == m.id, Attendance.status == "PRESENT"
        ).count()
        
        task_count = db.query(TaskAssignment).join(Task).filter(
            TaskAssignment.user_id == m.id, Task.status == "DONE"
        ).count()
        
        # Contribution Score formula
        contribution_score = (att_count * 10) + (task_count * 20)
        dept_name = m.department.name if m.department else "Chưa xếp ban"
        
        results.append({
            "user_id": m.id,
            "full_name": m.full_name,
            "department_name": dept_name,
            "role": m.role,
            "attendance_count": att_count,
            "task_completed_count": task_count,
            "contribution_score": contribution_score
        })
        
    results.sort(key=lambda x: x["contribution_score"], reverse=True)
    return jsonify(results), 200
