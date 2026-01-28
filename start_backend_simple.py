"""
Simple backend starter with better error handling
"""
import sys
import os
import traceback

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

print("=" * 60)
print("Starting Secure Notes Backend Server")
print("=" * 60)

try:
    # Test imports first
    print("\n[1] Testing imports...")
    from database.database import engine, DATABASE_URL
    from database import models
    from api import auth, notes
    print("    ✅ All imports successful")
    
    # Test database connection
    print("\n[2] Testing database connection...")
    with engine.connect() as conn:
        print("    ✅ Database connection successful")
    
    # Import app
    print("\n[3] Loading FastAPI application...")
    from main import app
    print("    ✅ FastAPI app loaded")
    
    print("\n[4] Starting server...")
    print("    Server will be available at: http://localhost:8000")
    print("    API docs: http://localhost:8000/docs")
    print("    Press Ctrl+C to stop the server")
    print("\n" + "=" * 60 + "\n")
    
    # Start server
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
    
except ImportError as e:
    print(f"\n❌ Import Error: {e}")
    print("\nPossible fixes:")
    print("1. Install missing packages: pip install -r requirements.txt")
    print("2. Make sure you're in the project root directory")
    traceback.print_exc()
    sys.exit(1)
    
except Exception as e:
    print(f"\n❌ Error starting server: {e}")
    print("\nFull error details:")
    traceback.print_exc()
    sys.exit(1)
