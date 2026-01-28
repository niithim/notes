"""
Quick test - just try to import and create the app
Shows the exact error if something fails
"""
import sys
import traceback

sys.path.insert(0, 'backend')

print("Quick Backend Test")
print("=" * 50)

try:
    print("\n1. Importing modules...")
    from database.database import engine, DATABASE_URL
    print("   ✅ database.database")
    
    from database import models
    print("   ✅ database.models")
    
    from api import auth
    print("   ✅ api.auth")
    
    from api import notes
    print("   ✅ api.notes")
    
    print("\n2. Creating FastAPI app...")
    from main import app
    print("   ✅ FastAPI app created")
    
    print("\n3. Testing database connection...")
    with engine.connect() as conn:
        print("   ✅ Database connection OK")
    
    print("\n✅ ALL TESTS PASSED!")
    print("\nThe backend should work. Try starting with:")
    print("   python start_backend_simple.py")
    
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    print("\nFull error details:")
    print("-" * 50)
    traceback.print_exc()
    print("-" * 50)
    print("\nPlease share this error message for help")
