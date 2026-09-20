from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text, nullable=True)

    members = relationship("User", back_populates="department")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(150), nullable=False)
    email = Column(String(150), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), default="MEMBER") # ADMIN, LEADER, MEMBER
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True)
    skills = Column(Text, default="[]") # JSON list of skills
    free_slots = Column(Text, default="[]") # JSON list of free time slots
    avatar_url = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    department = relationship("Department", back_populates="members")
    attendances = relationship("Attendance", back_populates="user")
    task_assignments = relationship("TaskAssignment", back_populates="user", foreign_keys="[TaskAssignment.user_id]")

class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=True)
    location = Column(String(200), nullable=True)
    latitude = Column(Float, default=21.028511)
    longitude = Column(Float, default=105.804817)
    radius_meters = Column(Float, default=100.0)
    status = Column(String(20), default="UPCOMING") # UPCOMING, ONGOING, COMPLETED
    qr_code_hash = Column(String(100), nullable=True)
    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    attendances = relationship("Attendance", back_populates="activity")
    tasks = relationship("Task", back_populates="activity")

class Attendance(Base):
    __tablename__ = "attendances"

    id = Column(Integer, primary_key=True, index=True)
    activity_id = Column(Integer, ForeignKey("activities.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    checkin_time = Column(DateTime, default=datetime.utcnow)
    status = Column(String(20), default="PRESENT") # PRESENT, LATE, ABSENT
    device_fingerprint = Column(String(255), nullable=True)

    activity = relationship("Activity", back_populates="attendances")
    user = relationship("User", back_populates="attendances")

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    activity_id = Column(Integer, ForeignKey("activities.id"), nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    required_skill = Column(String(100), nullable=True)
    deadline = Column(DateTime, nullable=True)
    status = Column(String(20), default="TO_DO") # TO_DO, IN_PROGRESS, DONE

    activity = relationship("Activity", back_populates="tasks")
    assignments = relationship("TaskAssignment", back_populates="task")

class TaskAssignment(Base):
    __tablename__ = "task_assignments"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    ai_suggested = Column(Boolean, default=False)
    match_score = Column(Float, default=1.0)
    assigned_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    assigned_at = Column(DateTime, default=datetime.utcnow)

    task = relationship("Task", back_populates="assignments")
    user = relationship("User", back_populates="task_assignments", foreign_keys=[user_id])

class AILog(Base):
    __tablename__ = "ai_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    prompt_type = Column(String(50), nullable=False) # ANNOUNCEMENT, SUMMARY, RECOMMEND
    input_data = Column(Text, nullable=False)
    output_result = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
