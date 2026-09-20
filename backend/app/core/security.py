import bcrypt
from datetime import datetime, timedelta
from typing import Optional, Any
from functools import wraps
from flask import request, jsonify, g
from jose import jwt, JWTError
from app.core.config import settings
from app.core.database import SessionLocal
from app.models.models import User

def get_password_hash(password: str) -> str:
    """Hash password using bcrypt."""
    salt = bcrypt.gensalt(rounds=12)
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify plain password against hashed password."""
    try:
        if hashed_password.startswith("$2b$") or hashed_password.startswith("$2a$"):
            return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
        # Fallback for plain/legacy sha256 if needed
        import hashlib
        salt = "bmad_club_salt_2026"
        return hashlib.sha256((plain_password + salt).encode('utf-8')).hexdigest() == hashed_password
    except Exception:
        return False

def create_access_token(subject: str | Any, expires_delta: Optional[timedelta] = None) -> str:
    """Generate signed JWT access token."""
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def jwt_required(f):
    """Decorator to protect Flask endpoints requiring a valid JWT token."""
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"detail": "Token xác thực không hợp lệ hoặc thiếu Authorization Header"}), 401
        
        token = auth_header.split(" ")[1]
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            user_id = payload.get("sub")
            if user_id is None:
                return jsonify({"detail": "Không thể giải mã danh tính người dùng từ token"}), 401
        except JWTError:
            return jsonify({"detail": "Token hết hạn hoặc không hợp lệ"}), 401
        
        db = SessionLocal()
        user = db.query(User).filter(User.id == int(user_id)).first()
        if not user:
            db.close()
            return jsonify({"detail": "Tài khoản người dùng không tồn tại"}), 401
            
        g.current_user = user
        g.db = db
        try:
            return f(*args, **kwargs)
        finally:
            db.close()
    return decorated

def roles_required(*allowed_roles):
    """Decorator to enforce RBAC permissions in Flask."""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            current_user = getattr(g, "current_user", None)
            if not current_user:
                return jsonify({"detail": "Chưa xác thực người dùng"}), 401
            if current_user.role not in allowed_roles:
                return jsonify({"detail": f"Không có quyền truy cập. Yêu cầu một trong các vai trò: {', '.join(allowed_roles)}"}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator
