from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# Token Schemas
class Token(BaseModel):
    access_token: str
    token_type: str
    user: "UserOut"

class TokenData(BaseModel):
    user_id: Optional[str] = None

# User Schemas
class UserBase(BaseModel):
    full_name: str
    email: EmailStr
    role: Optional[str] = "MEMBER"
    department_id: Optional[int] = None
    skills: Optional[List[str]] = []
    free_slots: Optional[List[str]] = []

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    role: Optional[str] = None
    department_id: Optional[int] = None
    skills: Optional[List[str]] = None
    free_slots: Optional[List[str]] = None

class UserOut(UserBase):
    id: int
    avatar_url: Optional[str] = None
    department_name: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True

# Department Schemas
class DepartmentBase(BaseModel):
    name: str
    description: Optional[str] = None

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentOut(DepartmentBase):
    id: int
    member_count: Optional[int] = 0

    class Config:
        from_attributes = True

# Activity Schemas
class ActivityBase(BaseModel):
    title: str
    description: Optional[str] = None
    start_time: datetime
    end_time: Optional[datetime] = None
    location: Optional[str] = None
    latitude: Optional[float] = 21.028511
    longitude: Optional[float] = 105.804817
    radius_meters: Optional[float] = 100.0
    status: Optional[str] = "UPCOMING"

class ActivityCreate(ActivityBase):
    pass

class ActivityOut(ActivityBase):
    id: int
    qr_code_hash: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    radius_meters: Optional[float] = None
    created_by: Optional[int] = None
    attendance_count: Optional[int] = 0

    class Config:
        from_attributes = True

# Attendance Schemas with Anti-Proxy Device Fingerprint & GPS
class AttendanceCheckin(BaseModel):
    activity_id: int
    qr_code_hash: Optional[str] = None
    user_lat: Optional[float] = None
    user_lng: Optional[float] = None
    device_fingerprint: Optional[str] = None

class AttendanceOut(BaseModel):
    id: int
    activity_id: int
    user_id: int
    user_name: Optional[str] = None
    checkin_time: datetime
    status: str

    class Config:
        from_attributes = True

# Task Schemas
class TaskBase(BaseModel):
    activity_id: int
    title: str
    description: Optional[str] = None
    required_skill: Optional[str] = None
    deadline: Optional[datetime] = None
    status: Optional[str] = "TO_DO"

class TaskCreate(TaskBase):
    pass

class TaskStatusUpdate(BaseModel):
    status: str

class TaskAssignmentCreate(BaseModel):
    task_id: int
    user_id: int
    ai_suggested: Optional[bool] = False
    match_score: Optional[float] = 1.0

class TaskOut(TaskBase):
    id: int
    assigned_user_id: Optional[int] = None
    assigned_user_name: Optional[str] = None
    ai_suggested: Optional[bool] = False
    match_score: Optional[float] = 1.0

    class Config:
        from_attributes = True

# AI Service Schemas
class AIAnnouncementRequest(BaseModel):
    activity_title: str
    activity_description: str
    start_time: str
    location: str
    tone: Optional[str] = "enthusiastic"

class AISummaryRequest(BaseModel):
    activity_title: str
    meeting_notes: str
    member_feedbacks: List[str] = []

class AIAssignmentRequest(BaseModel):
    activity_id: int
    task_ids: List[int]

class AIAssignmentItem(BaseModel):
    task_id: int
    task_title: str
    recommended_user_id: int
    recommended_user_name: str
    match_score: float
    reason: str

class AIAssignmentResponse(BaseModel):
    suggestions: List[AIAssignmentItem]
