import json
from datetime import datetime, timedelta
from app.core.database import SessionLocal, Base, engine
from app.core.security import get_password_hash
from app.models.models import Department, User, Activity, Attendance, Task, TaskAssignment

def seed_database(force=True):
    if force:
        Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    try:
        if not force and db.query(Department).count() > 0:
            print("Database already seeded!")
            return
            
        print("Seeding initial data with bcrypt password hashes...")
        
        # 1. Departments
        dept_tt = Department(name="Ban Truyền thông", description="Phụ trách thiết kế, viết bài, fanpage và truyền thông sự kiện")
        dept_sk = Department(name="Ban Sự kiện", description="Phụ trách lập kế hoạch, hậu cần, setup và điều phối sự kiện")
        dept_cm = Department(name="Ban Chuyên môn", description="Phụ trách nội dung đào tạo, hội thảo và hỗ trợ học tập")
        dept_dn = Department(name="Ban Đối ngoại", description="Phụ trách liên hệ tài trợ, đối tác và đón tiếp khách mời")
        
        db.add_all([dept_tt, dept_sk, dept_cm, dept_dn])
        db.commit()
        
        # 2. Users (Admin, Leader, Members)
        users_data = [
            {
                "full_name": "La Văn Quyền",
                "email": "admin@club.edu.vn",
                "password": "admin123",
                "role": "ADMIN",
                "department_id": dept_cm.id,
                "skills": ["Lập trình", "Quản lý", "Kiến trúc hệ thống"],
                "free_slots": ["Tối T2", "Tối T4", "Cả ngày T7"]
            },
            {
                "full_name": "Nguyễn Đức Anh",
                "email": "leader@club.edu.vn",
                "password": "leader123",
                "role": "LEADER",
                "department_id": dept_tt.id,
                "skills": ["Thiết kế Photoshop", "Viết bài Content", "Điều phối"],
                "free_slots": ["Sáng T3", "Tối T6", "Cả ngày CN"]
            },
            {
                "full_name": "Trần Phương Anh",
                "email": "member@club.edu.vn",
                "password": "member123",
                "role": "MEMBER",
                "department_id": dept_tt.id,
                "skills": ["Thiết kế Photoshop", "Canva", "Video Editing"],
                "free_slots": ["Tối T3", "Tối T5", "Chiều T7"]
            },
            {
                "full_name": "Trần Phương Anh",
                "email": "member1@club.edu.vn",
                "password": "user123",
                "role": "MEMBER",
                "department_id": dept_tt.id,
                "skills": ["Thiết kế Photoshop", "Canva", "Video Editing"],
                "free_slots": ["Tối T3", "Tối T5", "Chiều T7"]
            },
            {
                "full_name": "Lê Văn Hoàng",
                "email": "member2@club.edu.vn",
                "password": "user123",
                "role": "MEMBER",
                "department_id": dept_sk.id,
                "skills": ["Setup âm thanh", "MC dẫn chương trình", "Hậu cần"],
                "free_slots": ["Tối T4", "Cả ngày T7", "Cả ngày CN"]
            },
            {
                "full_name": "Phạm Thị Phương",
                "email": "member3@club.edu.vn",
                "password": "user123",
                "role": "MEMBER",
                "department_id": dept_cm.id,
                "skills": ["Thuyết trình", "Viết báo cáo", "Tiếng Anh"],
                "free_slots": ["Chiều T2", "Tối T6", "Sáng T7"]
            },
            {
                "full_name": "Đặng Minh Tuấn",
                "email": "member4@club.edu.vn",
                "password": "user123",
                "role": "MEMBER",
                "department_id": dept_dn.id,
                "skills": ["Giao tiếp", "Xin tài trợ", "Đón tiếp"],
                "free_slots": ["Tối T2", "Tối T4", "Tối T7"]
            }
        ]
        
        created_users = []
        for ud in users_data:
            u = User(
                full_name=ud["full_name"],
                email=ud["email"],
                password_hash=get_password_hash(ud["password"]),
                role=ud["role"],
                department_id=ud["department_id"],
                skills=json.dumps(ud["skills"]),
                free_slots=json.dumps(ud["free_slots"])
            )
            db.add(u)
            created_users.append(u)
            
        db.commit()
        
        # 3. Activities
        act1 = Activity(
            title="Chào tân sinh viên & Workshop AI 2026",
            description="Sự kiện chào mừng sinh viên khóa mới kết hợp chia sẻ ứng dụng AI trong học tập và làm việc.",
            start_time=datetime.utcnow() + timedelta(days=2),
            end_time=datetime.utcnow() + timedelta(days=2, hours=4),
            location="Hội trường A1 - Trường Đại học",
            status="UPCOMING",
            qr_code_hash="ACT_WELCOME_2026",
            created_by=created_users[0].id
        )
        
        act2 = Activity(
            title="Cuộc thi Hackathon CLB Sinh viên 2026",
            description="Thi lập trình nhanh và phát triển ứng dụng sáng tạo trong 24 giờ.",
            start_time=datetime.utcnow() - timedelta(days=5),
            end_time=datetime.utcnow() - timedelta(days=4),
            location="Phòng Lab Máy tính 302",
            status="COMPLETED",
            qr_code_hash="ACT_HACKATHON_2026",
            created_by=created_users[0].id
        )
        
        db.add_all([act1, act2])
        db.commit()
        
        # 4. Tasks for Activity 1
        t1 = Task(
            activity_id=act1.id,
            title="Thiết kế Banner & Poster sự kiện Chào Tân Sinh Viên",
            description="Thiết kế bộ nhận diện truyền thông kích thước 1920x1080px và Standee đứng.",
            required_skill="Thiết kế Photoshop",
            deadline=datetime.utcnow() + timedelta(days=1),
            status="IN_PROGRESS"
        )
        t2 = Task(
            activity_id=act1.id,
            title="Setup hệ thống âm thanh & Ánh sáng hội trường A1",
            description="Kiểm tra micro, loa, máy chiếu trước giờ G 2 tiếng.",
            required_skill="Setup âm thanh",
            deadline=datetime.utcnow() + timedelta(days=2),
            status="TO_DO"
        )
        t3 = Task(
            activity_id=act1.id,
            title="Soạn thảo bài đăng Truyền thông Fanpage",
            description="Viết nội dung giới thiệu diễn giả và lịch trình sự kiện.",
            required_skill="Viết bài Content",
            deadline=datetime.utcnow() + timedelta(days=1),
            status="DONE"
        )
        
        db.add_all([t1, t2, t3])
        db.commit()
        
        # 5. Task Assignments
        ta1 = TaskAssignment(task_id=t1.id, user_id=created_users[2].id, ai_suggested=True, match_score=0.95, assigned_by=created_users[0].id)
        ta2 = TaskAssignment(task_id=t2.id, user_id=created_users[3].id, ai_suggested=True, match_score=0.92, assigned_by=created_users[0].id)
        ta3 = TaskAssignment(task_id=t3.id, user_id=created_users[1].id, ai_suggested=False, match_score=0.88, assigned_by=created_users[0].id)
        
        db.add_all([ta1, ta2, ta3])
        
        # 6. Attendances for Act 2
        for u in created_users[:4]:
            att = Attendance(activity_id=act2.id, user_id=u.id, checkin_time=datetime.utcnow() - timedelta(days=5), status="PRESENT", device_fingerprint="browser_fingerprint_demo")
            db.add(att)
            
        db.commit()
        print("Database seeded successfully with clean bcrypt hashes!")
        
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_database(force=True)
