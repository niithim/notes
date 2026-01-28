"""
Test script to verify the setup is correct
Run this to check if all dependencies are installed and imports work
"""
import sys

print("Testing Secure Notes App Setup...")
print("=" * 50)

# Test 1: Python version
print("\n1. Checking Python version...")
version = sys.version_info
print(f"   Python {version.major}.{version.minor}.{version.micro}")
if version.major < 3 or (version.major == 3 and version.minor < 8):
    print("   ❌ Python 3.8+ required")
    sys.exit(1)
else:
    print("   ✅ Python version OK")

# Test 2: Check required packages
print("\n2. Checking required packages...")
required_packages = [
    'fastapi',
    'uvicorn',
    'sqlalchemy',
    'pydantic',
    'bcrypt',
    'jwt'
]

missing_packages = []
for package in required_packages:
    try:
        if package == 'jwt':
            __import__('jwt')
        else:
            __import__(package)
        print(f"   ✅ {package}")
    except ImportError:
        print(f"   ❌ {package} - NOT INSTALLED")
        missing_packages.append(package)

if missing_packages:
    print(f"\n   Missing packages: {', '.join(missing_packages)}")
    print("   Run: pip install -r requirements.txt")
    sys.exit(1)

# Test 3: Check backend imports
print("\n3. Testing backend imports...")
sys.path.insert(0, 'backend')

try:
    from database import models
    print("   ✅ database.models")
except Exception as e:
    print(f"   ❌ database.models - {e}")
    sys.exit(1)

try:
    from database.database import engine, get_db
    print("   ✅ database.database")
except Exception as e:
    print(f"   ❌ database.database - {e}")
    sys.exit(1)

try:
    from api import auth, notes
    print("   ✅ api.auth")
    print("   ✅ api.notes")
except Exception as e:
    print(f"   ❌ api modules - {e}")
    sys.exit(1)

# Test 4: Check main app
print("\n4. Testing main application...")
try:
    from main import app
    print("   ✅ FastAPI app created")
except Exception as e:
    print(f"   ❌ Failed to create app - {e}")
    sys.exit(1)

print("\n" + "=" * 50)
print("✅ All tests passed! Setup is correct.")
print("\nYou can now run the server with:")
print("  - python start_server.py (from root)")
print("  - cd backend && python main.py")
print("  - cd backend && uvicorn main:app --reload")
