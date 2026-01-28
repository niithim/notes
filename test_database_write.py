"""
Test script to verify database write operations
This will create a test user and note to verify data is being stored
"""
import sys
import os

sys.path.insert(0, 'backend')

print("=" * 60)
print("Testing Database Write Operations")
print("=" * 60)

try:
    from database.database import SessionLocal, DATABASE_URL
    from database import models
    import bcrypt
    
    print(f"\nDatabase location: {DATABASE_URL}")
    
    db = SessionLocal()
    
    try:
        # Test 1: Create a test user
        print("\n1. Creating test user...")
        test_email = "test@example.com"
        
        # Check if test user already exists
        existing = db.query(models.User).filter(models.User.email == test_email).first()
        if existing:
            print(f"   Test user already exists (ID: {existing.id})")
            test_user = existing
        else:
            # Hash password
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw("testpass123".encode('utf-8'), salt)
            
            test_user = models.User(
                name="Test User",
                email=test_email,
                hashed_password=hashed.decode('utf-8')
            )
            db.add(test_user)
            db.commit()
            db.refresh(test_user)
            print(f"   ✅ Test user created (ID: {test_user.id})")
        
        # Test 2: Create a test note
        print("\n2. Creating test note...")
        test_note = models.Note(
            user_id=test_user.id,
            title="Test Note",
            content="This is a test note to verify database storage is working."
        )
        db.add(test_note)
        db.commit()
        db.refresh(test_note)
        print(f"   ✅ Test note created (ID: {test_note.id})")
        
        # Test 3: Verify data was saved
        print("\n3. Verifying data was saved...")
        db.close()
        
        # Open new session to verify
        db2 = SessionLocal()
        saved_user = db2.query(models.User).filter(models.User.id == test_user.id).first()
        saved_note = db2.query(models.Note).filter(models.Note.id == test_note.id).first()
        
        if saved_user:
            print(f"   ✅ User found in database: {saved_user.name} ({saved_user.email})")
        else:
            print("   ❌ User NOT found in database!")
        
        if saved_note:
            print(f"   ✅ Note found in database: {saved_note.title}")
        else:
            print("   ❌ Note NOT found in database!")
        
        # Count all records
        user_count = db2.query(models.User).count()
        note_count = db2.query(models.Note).count()
        print(f"\n   Total users: {user_count}")
        print(f"   Total notes: {note_count}")
        
        db2.close()
        
        print("\n" + "=" * 60)
        print("✅ Database write test completed successfully!")
        print("=" * 60)
        print("\nIf you see ✅ above, database storage is working correctly.")
        print("If data is still not saving in the app, check:")
        print("1. Backend server is running")
        print("2. API endpoints are being called (check browser console)")
        print("3. No errors in backend terminal")
        
    except Exception as e:
        db.rollback()
        print(f"\n❌ Error during database operation: {e}")
        import traceback
        traceback.print_exc()
        raise
        
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
