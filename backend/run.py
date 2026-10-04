import sys
import os

# Add backend directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.main import app
from app.core.config import settings

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

if __name__ == "__main__":
    port = int(getattr(settings, "PORT", 5000))
    print(f"Starting Flask Server on http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=True)
