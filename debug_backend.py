"""
Comprehensive Backend Debugging Script
Run this to identify why the backend won't start
"""
import sys
import os
import traceback

print("=" * 70)
print("BACKEND DEBUGGING - Finding the Issue")
print("=" * 70)

# Add backend to path
sys.path.insert(0, 'backend')

errors_found = []
warnings_found = []

# Test 1: Check if we're in the right directory
print("\n[1] Checking Current Directory...")
current_dir = os.getcwd()
print(f"    Current directory: {current_dir}")
if not os.path.exists('backend'):
    errors_found.append("'backend' folder not found in current directory")
    print("    ❌ 'backend' folder not found!")
    print("    Please run this script from the project root directory")
    sys.exit(1)
else:
    print("    ✅ 'backend' folder found")

# Test 2: Check backend files
print("\n[2] Checking Backend Files...")
required_files = {
    'backend/main.py': 'Main application file',
    'backend/database/database.py': 'Database configuration',
    'backend/database/models.py': 'Database models',
    'backend/api/auth.py': 'Authentication API',
    'backend/api/notes.py': 'Notes API'
}

for file_path, description in required_files.items():
    if os.path.exists(file_path):
        print(f"    ✅ {file_path}")
    else:
        errors_found.append(f"Missing: {file_path}")
        print(f"    ❌ {file_path} - MISSING")

# Test 3: Check Python packages
print("\n[3] Checking Python Packages...")
packages = {
    'fastapi': 'FastAPI',
    'uvicorn': 'Uvicorn',
    'sqlalchemy': 'SQLAlchemy',
    'pydantic': 'Pydantic',
    'bcrypt': 'bcrypt',
    'jwt': 'PyJWT',
    'pymysql': 'PyMySQL'
}

missing_packages = []
for module, name in packages.items():
    try:
        if module == 'jwt':
            __import__('jwt')
        else:
            __import__(module)
        print(f"    ✅ {name}")
    except ImportError:
        missing_packages.append(name)
        errors_found.append(f"Missing package: {name}")
        print(f"    ❌ {name} - NOT INSTALLED")

if missing_packages:
    print(f"\n    ⚠️  Install missing packages:")
    print(f"    pip install {' '.join(missing_packages)}")

# Test 4: Try importing database module
print("\n[4] Testing Database Module Import...")
try:
    from database.database import engine, DATABASE_URL, SessionLocal, Base
    print(f"    ✅ Database module imported successfully")
    print(f"    Database URL: {DATABASE_URL.split('@')[0]}@****")
except Exception as e:
    errors_found.append(f"Database import error: {str(e)}")
    print(f"    ❌ Database import failed: {e}")
    print("\n    Full error:")
    traceback.print_exc()

# Test 5: Try importing models
print("\n[5] Testing Models Import...")
try:
    from database import models
    print(f"    ✅ Models imported successfully")
    print(f"    User model: {'✅' if hasattr(models, 'User') else '❌'}")
    print(f"    Note model: {'✅' if hasattr(models, 'Note') else '❌'}")
except Exception as e:
    errors_found.append(f"Models import error: {str(e)}")
    print(f"    ❌ Models import failed: {e}")
    print("\n    Full error:")
    traceback.print_exc()

# Test 6: Try importing API modules
print("\n[6] Testing API Modules Import...")
try:
    from api import auth
    print(f"    ✅ auth module imported")
except Exception as e:
    errors_found.append(f"auth import error: {str(e)}")
    print(f"    ❌ auth import failed: {e}")
    traceback.print_exc()

try:
    from api import notes
    print(f"    ✅ notes module imported")
except Exception as e:
    errors_found.append(f"notes import error: {str(e)}")
    print(f"    ❌ notes import failed: {e}")
    traceback.print_exc()

# Test 7: Try creating FastAPI app
print("\n[7] Testing FastAPI App Creation...")
try:
    from main import app
    print(f"    ✅ FastAPI app created successfully")
    print(f"    App title: {app.title}")
    print(f"    Number of routes: {len(app.routes)}")
except Exception as e:
    errors_found.append(f"FastAPI app creation error: {str(e)}")
    print(f"    ❌ FastAPI app creation failed: {e}")
    print("\n    Full error traceback:")
    traceback.print_exc()

# Test 8: Check MySQL connection (if applicable)
print("\n[8] Testing MySQL Connection...")
try:
    from database.database import engine, DATABASE_URL
    if DATABASE_URL.startswith("mysql"):
        print(f"    Attempting to connect to MySQL...")
        with engine.connect() as conn:
            print(f"    ✅ MySQL connection successful!")
    else:
        print(f"    Using {DATABASE_URL.split('://')[0]} database (not MySQL)")
except Exception as e:
    warnings_found.append(f"Database connection warning: {str(e)}")
    print(f"    ⚠️  Database connection issue: {e}")
    print("    (This might be OK if MySQL is not running yet)")

# Test 9: Try to start uvicorn (dry run)
print("\n[9] Testing Server Startup (Dry Run)...")
try:
    import uvicorn
    from main import app
    print(f"    ✅ Uvicorn available")
    print(f"    ✅ App can be loaded")
    print(f"    Ready to start on: http://0.0.0.0:8000")
except Exception as e:
    errors_found.append(f"Server startup test error: {str(e)}")
    print(f"    ❌ Server startup test failed: {e}")
    traceback.print_exc()

# Summary
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

if errors_found:
    print(f"\n❌ Found {len(errors_found)} ERROR(S):")
    for i, error in enumerate(errors_found, 1):
        print(f"   {i}. {error}")
    print("\n⚠️  BACKEND WILL NOT START until these errors are fixed!")
else:
    print("\n✅ No critical errors found!")

if warnings_found:
    print(f"\n⚠️  Found {len(warnings_found)} WARNING(S):")
    for i, warning in enumerate(warnings_found, 1):
        print(f"   {i}. {warning}")

if not errors_found:
    print("\n" + "=" * 70)
    print("✅ BACKEND SHOULD BE READY TO RUN!")
    print("=" * 70)
    print("\nTry starting the server with:")
    print("   python start_server.py")
    print("\nOr:")
    print("   cd backend")
    print("   python main.py")
else:
    print("\n" + "=" * 70)
    print("❌ FIX ERRORS BEFORE STARTING")
    print("=" * 70)
    print("\nCommon fixes:")
    if any("Missing package" in e for e in errors_found):
        print("   1. Install missing packages: pip install -r requirements.txt")
    if any("import" in e.lower() for e in errors_found):
        print("   2. Check that all __init__.py files exist")
        print("   3. Make sure you're running from the project root")
    if any("MySQL" in e or "database" in e.lower() for e in errors_found):
        print("   4. Make sure MySQL is running")
        print("   5. Run: python setup_mysql.py")

print("\n" + "=" * 70)
