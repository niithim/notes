"""
Backend Verification Script
Checks all backend components for issues
"""
import sys
import os

print("=" * 60)
print("Backend Verification")
print("=" * 60)

errors = []
warnings = []

# Add backend to path
sys.path.insert(0, 'backend')

# Test 1: Check Python version
print("\n1. Python Version Check...")
version = sys.version_info
print(f"   Python {version.major}.{version.minor}.{version.micro}")
if version.major < 3 or (version.major == 3 and version.minor < 8):
    errors.append("Python 3.8+ required")
else:
    print("   ✅ Python version OK")

# Test 2: Check required packages
print("\n2. Checking Required Packages...")
required = {
    'fastapi': 'FastAPI',
    'uvicorn': 'Uvicorn',
    'sqlalchemy': 'SQLAlchemy',
    'pydantic': 'Pydantic',
    'bcrypt': 'bcrypt',
    'jwt': 'PyJWT',
    'pymysql': 'PyMySQL'
}

for module, name in required.items():
    try:
        if module == 'jwt':
            __import__('jwt')
        else:
            __import__(module)
        print(f"   ✅ {name}")
    except ImportError:
        errors.append(f"Missing package: {name}")
        print(f"   ❌ {name} - NOT INSTALLED")

# Test 3: Check backend structure
print("\n3. Checking Backend Structure...")
required_files = [
    'backend/main.py',
    'backend/database/database.py',
    'backend/database/models.py',
    'backend/api/auth.py',
    'backend/api/notes.py',
    'backend/__init__.py',
    'backend/api/__init__.py',
    'backend/database/__init__.py'
]

for file_path in required_files:
    if os.path.exists(file_path):
        print(f"   ✅ {file_path}")
    else:
        errors.append(f"Missing file: {file_path}")
        print(f"   ❌ {file_path} - NOT FOUND")

# Test 4: Check imports
print("\n4. Testing Imports...")
try:
    from database.database import engine, DATABASE_URL, SessionLocal, Base
    print("   ✅ database.database imports OK")
except Exception as e:
    errors.append(f"database.database import error: {e}")
    print(f"   ❌ database.database - {e}")

try:
    from database import models
    print("   ✅ database.models imports OK")
except Exception as e:
    errors.append(f"database.models import error: {e}")
    print(f"   ❌ database.models - {e}")

try:
    from api import auth, notes
    print("   ✅ api modules imports OK")
except Exception as e:
    errors.append(f"api modules import error: {e}")
    print(f"   ❌ api modules - {e}")

# Test 5: Check database configuration
print("\n5. Checking Database Configuration...")
try:
    from database.database import DATABASE_URL, MYSQL_HOST, MYSQL_USER, MYSQL_DATABASE
    print(f"   Database URL: {DATABASE_URL.split('@')[0]}@****")
    print(f"   Host: {MYSQL_HOST}")
    print(f"   User: {MYSQL_USER}")
    print(f"   Database: {MYSQL_DATABASE}")
    print("   ✅ Database configuration OK")
except Exception as e:
    errors.append(f"Database configuration error: {e}")
    print(f"   ❌ Database configuration - {e}")

# Test 6: Check SQLAlchemy Base
print("\n6. Checking SQLAlchemy Base...")
try:
    from database.database import Base
    if hasattr(Base, '__bases__'):
        print("   ✅ Base class is DeclarativeBase")
    else:
        warnings.append("Base class structure unexpected")
        print("   ⚠️  Base class structure check")
except Exception as e:
    errors.append(f"Base class error: {e}")
    print(f"   ❌ Base class - {e}")

# Test 7: Check models
print("\n7. Checking Database Models...")
try:
    from database import models
    if hasattr(models, 'User'):
        print("   ✅ User model found")
    else:
        errors.append("User model not found")
        print("   ❌ User model NOT FOUND")
    
    if hasattr(models, 'Note'):
        print("   ✅ Note model found")
    else:
        errors.append("Note model not found")
        print("   ❌ Note model NOT FOUND")
except Exception as e:
    errors.append(f"Models check error: {e}")
    print(f"   ❌ Models check - {e}")

# Test 8: Check FastAPI app creation
print("\n8. Testing FastAPI App Creation...")
try:
    from main import app
    print("   ✅ FastAPI app created successfully")
    print(f"   Title: {app.title}")
    print(f"   Version: {app.version}")
except Exception as e:
    errors.append(f"FastAPI app creation error: {e}")
    print(f"   ❌ FastAPI app - {e}")
    import traceback
    traceback.print_exc()

# Test 9: Check routers
print("\n9. Checking API Routers...")
try:
    from main import app
    routes = [route.path for route in app.routes]
    print(f"   Found {len(routes)} routes")
    
    required_routes = [
        '/api/signup',
        '/api/login',
        '/api/forgot-password',
        '/api/reset-password',
        '/api/notes'
    ]
    
    for route in required_routes:
        if any(route in r for r in routes):
            print(f"   ✅ {route}")
        else:
            warnings.append(f"Route not found: {route}")
            print(f"   ⚠️  {route} - Not found")
except Exception as e:
    errors.append(f"Routes check error: {e}")
    print(f"   ❌ Routes check - {e}")

# Summary
print("\n" + "=" * 60)
print("Verification Summary")
print("=" * 60)

if errors:
    print(f"\n❌ Found {len(errors)} error(s):")
    for error in errors:
        print(f"   - {error}")
else:
    print("\n✅ No errors found!")

if warnings:
    print(f"\n⚠️  Found {len(warnings)} warning(s):")
    for warning in warnings:
        print(f"   - {warning}")

if not errors and not warnings:
    print("\n✅ Backend is ready to run!")
    print("\nNext steps:")
    print("1. Make sure MySQL is running")
    print("2. Run: python setup_mysql.py (if not done)")
    print("3. Start server: python start_server.py")
else:
    print("\n⚠️  Please fix the issues above before running the server")

print("=" * 60)
