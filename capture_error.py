"""
Error Capture Script
This will try to start the backend and capture any errors
"""
import sys
import os
import traceback
from datetime import datetime

# Add backend to path
sys.path.insert(0, 'backend')

error_log = []

def log(msg):
    print(msg)
    error_log.append(msg)

log("=" * 70)
log(f"Error Capture - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
log("=" * 70)

try:
    log("\n[1] Testing imports...")
    from database.database import engine, DATABASE_URL, SessionLocal, Base
    log("    ✅ database.database imported")
    
    from database import models
    log("    ✅ database.models imported")
    
    from api import auth
    log("    ✅ api.auth imported")
    
    from api import notes
    log("    ✅ api.notes imported")
    
except Exception as e:
    log(f"\n❌ IMPORT ERROR: {e}")
    log("\nFull traceback:")
    log(traceback.format_exc())
    with open('error_log.txt', 'w') as f:
        f.write('\n'.join(error_log))
    sys.exit(1)

try:
    log("\n[2] Testing database connection...")
    with engine.connect() as conn:
        log("    ✅ Database connection successful")
except Exception as e:
    log(f"\n⚠️  DATABASE CONNECTION WARNING: {e}")
    log("    (This might be OK if MySQL is not running)")

try:
    log("\n[3] Testing FastAPI app creation...")
    from main import app
    log("    ✅ FastAPI app created")
    log(f"    App title: {app.title}")
    log(f"    Routes: {len(app.routes)}")
except Exception as e:
    log(f"\n❌ APP CREATION ERROR: {e}")
    log("\nFull traceback:")
    log(traceback.format_exc())
    with open('error_log.txt', 'w') as f:
        f.write('\n'.join(error_log))
    sys.exit(1)

try:
    log("\n[4] Testing table creation...")
    from database.database import engine
    from database import models
    models.Base.metadata.create_all(bind=engine)
    log("    ✅ Tables created/verified")
except Exception as e:
    log(f"\n❌ TABLE CREATION ERROR: {e}")
    log("\nFull traceback:")
    log(traceback.format_exc())
    with open('error_log.txt', 'w') as f:
        f.write('\n'.join(error_log))
    sys.exit(1)

try:
    log("\n[5] Testing SQLAlchemy queries...")
    from database.database import SessionLocal
    from database import models
    from sqlalchemy import select
    
    db = SessionLocal()
    try:
        # Test a simple query
        stmt = select(models.User)
        result = db.execute(stmt)
        log("    ✅ SQLAlchemy query syntax OK")
    except Exception as e:
        log(f"\n❌ SQLALCHEMY QUERY ERROR: {e}")
        log("\nFull traceback:")
        log(traceback.format_exc())
    finally:
        db.close()
except Exception as e:
    log(f"\n❌ QUERY TEST ERROR: {e}")
    log("\nFull traceback:")
    log(traceback.format_exc())

log("\n" + "=" * 70)
log("Testing Complete")
log("=" * 70)

# Try to actually start the server
log("\n[6] Attempting to start server...")
log("    (This will show any startup errors)")
log("")

try:
    import uvicorn
    from main import app
    
    log("Starting server on http://0.0.0.0:8000")
    log("Press Ctrl+C after a few seconds to stop")
    log("")
    
    # Start server (will run until interrupted)
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
    
except KeyboardInterrupt:
    log("\n\nServer stopped by user")
except Exception as e:
    log(f"\n❌ SERVER START ERROR: {e}")
    log("\nFull traceback:")
    log(traceback.format_exc())
    with open('error_log.txt', 'w') as f:
        f.write('\n'.join(error_log))
    log("\n✅ Error saved to error_log.txt")
    sys.exit(1)
