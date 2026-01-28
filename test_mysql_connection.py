"""
Test MySQL connection from Python
This verifies that Python can connect to MySQL with the configured credentials
"""
import sys
import os

sys.path.insert(0, 'backend')

print("=" * 60)
print("Testing MySQL Connection from Python")
print("=" * 60)

try:
    # Test 1: Import pymysql
    print("\n[1] Testing PyMySQL import...")
    import pymysql
    print("    ✅ PyMySQL imported successfully")
except ImportError:
    print("    ❌ PyMySQL not installed")
    print("    Install with: pip install pymysql")
    sys.exit(1)

try:
    # Test 2: Import database configuration
    print("\n[2] Loading database configuration...")
    from database.database import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE, DATABASE_URL
    print(f"    Host: {MYSQL_HOST}")
    print(f"    Port: {MYSQL_PORT}")
    print(f"    User: {MYSQL_USER}")
    print(f"    Password: {'*' * len(MYSQL_PASSWORD)}")
    print(f"    Database: {MYSQL_DATABASE}")
    print("    ✅ Configuration loaded")
except Exception as e:
    print(f"    ❌ Configuration error: {e}")
    sys.exit(1)

try:
    # Test 3: Direct connection test
    print("\n[3] Testing direct MySQL connection...")
    connection = pymysql.connect(
        host=MYSQL_HOST,
        port=int(MYSQL_PORT),
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        charset='utf8mb4'
    )
    print("    ✅ Direct connection successful!")
    connection.close()
except Exception as e:
    print(f"    ❌ Direct connection failed: {e}")
    print("    Check MySQL credentials in backend/database/database.py")
    sys.exit(1)

try:
    # Test 4: SQLAlchemy engine connection
    print("\n[4] Testing SQLAlchemy engine connection...")
    from database.database import engine
    with engine.connect() as conn:
        result = conn.execute("SELECT 1 as test")
        row = result.fetchone()
        if row and row[0] == 1:
            print("    ✅ SQLAlchemy engine connection successful!")
except Exception as e:
    print(f"    ❌ SQLAlchemy connection failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

try:
    # Test 5: Database exists check
    print("\n[5] Checking if database exists...")
    connection = pymysql.connect(
        host=MYSQL_HOST,
        port=int(MYSQL_PORT),
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        charset='utf8mb4'
    )
    with connection.cursor() as cursor:
        cursor.execute("SHOW DATABASES LIKE %s", (MYSQL_DATABASE,))
        result = cursor.fetchone()
        if result:
            print(f"    ✅ Database '{MYSQL_DATABASE}' exists")
        else:
            print(f"    ⚠️  Database '{MYSQL_DATABASE}' does not exist")
            print(f"    Run: python setup_mysql.py")
    connection.close()
except Exception as e:
    print(f"    ⚠️  Could not check database: {e}")

print("\n" + "=" * 60)
print("✅ MySQL Connection Test Complete!")
print("=" * 60)
print("\nIf all tests passed, your backend should be able to connect to MySQL.")
print("\nNext step: Start the backend server")
print("   python start_server.py")
