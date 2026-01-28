"""
Script to check if database is working and data is being stored
Run this to verify database operations
"""
import sys
import os

# Add backend to path
sys.path.insert(0, 'backend')

print("=" * 60)
print("Database Check Script")
print("=" * 60)

try:
    from database.database import engine, DATABASE_URL, SessionLocal
    from database import models
    
    print(f"\n1. Database URL: {DATABASE_URL}")
    
    # Check database type
    if DATABASE_URL.startswith("sqlite"):
        db_file = DATABASE_URL.replace('sqlite:///', '')
        if os.path.exists(db_file):
            file_size = os.path.getsize(db_file)
            print(f"   ✅ Database file exists ({file_size} bytes)")
        else:
            print(f"   ⚠️  Database file does not exist yet (will be created on first use)")
    elif DATABASE_URL.startswith("mysql"):
        print(f"   ✅ Using MySQL database")
        # Extract database name from URL
        if "/" in DATABASE_URL:
            db_name = DATABASE_URL.split("/")[-1].split("?")[0]
            print(f"   Database name: {db_name}")
    else:
        print(f"   ✅ Using database: {DATABASE_URL.split('://')[0]}")
    
    # Check if tables exist
    print("\n2. Checking database tables...")
    from sqlalchemy import inspect
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    
    if 'users' in tables:
        print("   ✅ 'users' table exists")
    else:
        print("   ❌ 'users' table NOT found")
    
    if 'notes' in tables:
        print("   ✅ 'notes' table exists")
    else:
        print("   ❌ 'notes' table NOT found")
    
    # Try to query data
    print("\n3. Checking stored data...")
    db = SessionLocal()
    try:
        user_count = db.query(models.User).count()
        note_count = db.query(models.Note).count()
        
        print(f"   Users in database: {user_count}")
        print(f"   Notes in database: {note_count}")
        
        if user_count > 0:
            print("\n   Sample users:")
            users = db.query(models.User).limit(3).all()
            for user in users:
                print(f"      - ID: {user.id}, Name: {user.name}, Email: {user.email}")
        
        if note_count > 0:
            print("\n   Sample notes:")
            notes = db.query(models.Note).limit(3).all()
            for note in notes:
                print(f"      - ID: {note.id}, Title: {note.title[:30]}..., User ID: {note.user_id}")
        
    except Exception as e:
        print(f"   ❌ Error querying database: {e}")
    finally:
        db.close()
    
    print("\n" + "=" * 60)
    print("✅ Database check complete!")
    print("=" * 60)
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
