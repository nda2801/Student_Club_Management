import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from app.core.config import settings

def get_engine():
    db_url = settings.DATABASE_URL
    try:
        if "postgresql" in db_url:
            eng = create_engine(db_url, pool_pre_ping=True, pool_size=10, max_overflow=20)
            # Test connection
            with eng.connect() as conn:
                pass
            return eng
        else:
            return create_engine(db_url, connect_args={"check_same_thread": False})
    except Exception as e:
        # Fallback to local SQLite file with deterministic absolute path
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        sqlite_path = os.path.join(base_dir, "student_club.db")
        return create_engine(f"sqlite:///{sqlite_path}", connect_args={"check_same_thread": False})

engine = get_engine()
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        pass
