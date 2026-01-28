"""
Diagnostic script - writes errors to error_log.txt
Run this to capture any errors
"""
import sys
import traceback
from datetime import datetime

error_log = []

def log(message):
    """Log a message"""
    print(message)
    error_log.append(message)

log("=" * 60)
log(f"Diagnostic Check - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
log("=" * 60)

# Test 1: Python version
log("\n1. Python Version:")
log(f"   {sys.version}")

# Test 2: Check if we're in the right directory
import os
log("\n2. Current Directory:")
log(f"   {os.getcwd()}")

# Test 3: Check if backend directory exists
log("\n3. Directory Structure:")
backend_exists = os.path.exists('backend')
log(f"   backend/ exists: {backend_exists}")

if backend_exists:
    api_exists = os.path.exists('backend/api')
    db_exists = os.path.exists('backend/database')
    log(f"   backend/api/ exists: {api_exists}")
    log(f"   backend/database/ exists: {db_exists}")

# Test 4: Check required packages
log("\n4. Checking Packages:")
packages_to_check = {
    'fastapi': 'FastAPI',
    'uvicorn': 'Uvicorn',
    'sqlalchemy': 'SQLAlchemy',
    'pydantic': 'Pydantic',
    'bcrypt': 'bcrypt',
    'jwt': 'PyJWT'
}

for module, name in packages_to_check.items():
    try:
        if module == 'jwt':
            import jwt
        else:
            __import__(module)
        log(f"   ✅ {name}")
    except ImportError as e:
        log(f"   ❌ {name} - NOT FOUND")
        log(f"      Error: {str(e)}")

# Test 5: Try importing backend modules
log("\n5. Testing Backend Imports:")
sys.path.insert(0, 'backend')

try:
    from database import models
    log("   ✅ database.models")
except Exception as e:
    log(f"   ❌ database.models")
    log(f"      Error: {str(e)}")
    log(f"      Traceback: {traceback.format_exc()}")

try:
    from database.database import engine, get_db
    log("   ✅ database.database")
except Exception as e:
    log(f"   ❌ database.database")
    log(f"      Error: {str(e)}")
    log(f"      Traceback: {traceback.format_exc()}")

try:
    from api import auth
    log("   ✅ api.auth")
except Exception as e:
    log(f"   ❌ api.auth")
    log(f"      Error: {str(e)}")
    log(f"      Traceback: {traceback.format_exc()}")

try:
    from api import notes
    log("   ✅ api.notes")
except Exception as e:
    log(f"   ❌ api.notes")
    log(f"      Error: {str(e)}")
    log(f"      Traceback: {traceback.format_exc()}")

# Test 6: Try creating the app
log("\n6. Testing App Creation:")
try:
    sys.path.insert(0, 'backend')
    from main import app
    log("   ✅ FastAPI app created successfully")
except Exception as e:
    log(f"   ❌ Failed to create app")
    log(f"      Error: {str(e)}")
    log(f"      Traceback: {traceback.format_exc()}")

# Write to file
log("\n" + "=" * 60)
log("Diagnostic complete!")

with open('error_log.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(error_log))

print(f"\n✅ Results saved to: error_log.txt")
print("   Please open error_log.txt to see the full diagnostic report")
