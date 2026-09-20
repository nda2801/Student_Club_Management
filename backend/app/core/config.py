import os
from pathlib import Path
from dotenv import load_dotenv

# 1. Tự động tìm và đọc file .env tổng ở thư mục gốc (Root Single Source of Truth)
_root_env = Path(__file__).resolve().parents[3] / ".env"
if _root_env.exists():
    load_dotenv(_root_env)

# 2. Đọc file backend/.env nếu người dùng muốn ghi đè riêng cho backend
_backend_env = Path(__file__).resolve().parents[2] / ".env"
if _backend_env.exists():
    load_dotenv(_backend_env, override=True)

# 3. Fallback đọc mặc định theo thư mục làm việc hiện hành
load_dotenv()

class Settings:
    PROJECT_NAME: str = "Hệ thống Quản lý CLB Sinh viên Tích hợp AI"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "bmad-super-secret-key-student-club-2026")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 # 7 days
    
    # Database: Default to PostgreSQL (with SQLite local fallback if specified or during offline testing)
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/student_club"
    )
    
    # AI Engine Keys
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "").strip()
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "").strip()
    
    # Server Port
    PORT: int = int(os.getenv("PORT", 5000))
    HOST: str = os.getenv("HOST", "0.0.0.0")

settings = Settings()
