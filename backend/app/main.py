from flask import Flask, jsonify
from flask_cors import CORS
from app.core.config import settings
from app.core.database import Base, engine, SessionLocal
from app.api.auth import router as auth_router
from app.api.members import router as members_router
from app.api.departments import router as departments_router
from app.api.activities import router as activities_router
from app.api.tasks import router as tasks_router
from app.api.ai import router as ai_router
from app.api.stats import router as stats_router

def create_app():
    # Initialize DB tables and seed initial demo data if empty
    try:
        Base.metadata.create_all(bind=engine)
        from app.models.models import User
        db = SessionLocal()
        try:
            if db.query(User).count() == 0:
                print("No users found. Auto-seeding initial database...")
                from seed_data import seed_database
                seed_database(force=False)
        finally:
            db.close()
    except Exception as e:
        print(f"[Warning] DB table creation / seed exception: {e}")
        
    app = Flask(__name__)
    
    # Configure Flask App
    app.config["SECRET_KEY"] = settings.SECRET_KEY
    app.config["JSON_AS_ASCII"] = False
    
    # Enable CORS
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
    
    # Register Blueprints
    api_prefix = settings.API_V1_STR # /api/v1
    app.register_blueprint(auth_router, url_prefix=f"{api_prefix}/auth")
    app.register_blueprint(members_router, url_prefix=f"{api_prefix}/members")
    app.register_blueprint(departments_router, url_prefix=f"{api_prefix}/departments")
    app.register_blueprint(activities_router, url_prefix=f"{api_prefix}/activities")
    app.register_blueprint(tasks_router, url_prefix=f"{api_prefix}/tasks")
    app.register_blueprint(ai_router, url_prefix=f"{api_prefix}/ai")
    app.register_blueprint(stats_router, url_prefix=f"{api_prefix}/stats")
    
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        SessionLocal.remove()
        
    @app.route("/", methods=["GET"])
    def root():
        return jsonify({
            "message": "Welcome to Student Club Management System API (Flask + PostgreSQL + Pydantic + JWT)",
            "status": "online",
            "version": "1.0.0"
        })
        
    @app.route("/api/health", methods=["GET"])
    def health_check():
        return jsonify({
            "status": "healthy",
            "database": "connected",
            "backend": "Flask",
            "auth": "JWT"
        }), 200
        
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"detail": "Endpoint not found"}), 404
        
    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({"detail": f"Internal server error: {str(e)}"}), 500
        
    return app

app = create_app()

if __name__ == "__main__":
    app.run(host=settings.HOST, port=settings.PORT, debug=True)
