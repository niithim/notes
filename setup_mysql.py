"""
Script to set up MySQL database for Secure Notes App
This will create the database and verify the connection
"""
import pymysql
import sys
import os

# MySQL Configuration
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", "3306"))
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "Nithin@123")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "secure_notes")

print("=" * 60)
print("MySQL Database Setup for Secure Notes App")
print("=" * 60)
print(f"\nConfiguration:")
print(f"  Host: {MYSQL_HOST}")
print(f"  Port: {MYSQL_PORT}")
print(f"  User: {MYSQL_USER}")
print(f"  Password: {'*' * len(MYSQL_PASSWORD)}")
print(f"  Database: {MYSQL_DATABASE}")
print()

try:
    # Step 1: Connect to MySQL server (without database)
    print("Step 1: Connecting to MySQL server...")
    connection = pymysql.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        charset='utf8mb4'
    )
    print("   ✅ Connected to MySQL server")
    
    # Step 2: Create database if it doesn't exist
    print(f"\nStep 2: Creating database '{MYSQL_DATABASE}' if it doesn't exist...")
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {MYSQL_DATABASE} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        connection.commit()
    print(f"   ✅ Database '{MYSQL_DATABASE}' is ready")
    
    # Step 3: Verify connection to the database
    print(f"\nStep 3: Verifying connection to database...")
    connection.close()
    
    connection = pymysql.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
        charset='utf8mb4'
    )
    print(f"   ✅ Successfully connected to database '{MYSQL_DATABASE}'")
    
    # Step 4: Check if tables exist
    print(f"\nStep 4: Checking existing tables...")
    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        if tables:
            print(f"   Found {len(tables)} table(s):")
            for table in tables:
                print(f"      - {table[0]}")
        else:
            print("   No tables found (they will be created when you start the server)")
    
    connection.close()
    
    print("\n" + "=" * 60)
    print("✅ MySQL setup completed successfully!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Install Python dependencies: pip install -r requirements.txt")
    print("2. Start the backend server: python start_server.py")
    print("3. Tables will be created automatically on first run")
    print()
    
except pymysql.Error as e:
    print(f"\n❌ MySQL Error: {e}")
    print("\nTroubleshooting:")
    print("1. Make sure MySQL server is running")
    print("2. Check username and password")
    print("3. Verify MySQL is accessible on the specified host and port")
    print("4. Make sure the MySQL user has CREATE DATABASE privileges")
    sys.exit(1)
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
