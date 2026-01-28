# How to Start the Backend - Step by Step

## Quick Fix First

Run this to automatically fix common issues:
```bash
python fix_backend.bat
```

Or manually:
```bash
pip install --upgrade -r requirements.txt
python debug_backend.py
```

## Step-by-Step Startup

### Step 1: Check What's Wrong
```bash
python debug_backend.py
```

This will tell you exactly what's preventing the backend from starting.

### Step 2: Fix Common Issues

#### Issue: Missing Packages
```bash
pip install -r requirements.txt
```

#### Issue: Python Cache Problems
```bash
# Windows
rmdir /s /q backend\__pycache__
rmdir /s /q backend\api\__pycache__
rmdir /s /q backend\database\__pycache__

# Linux/Mac
find . -type d -name __pycache__ -exec rm -r {} +
```

#### Issue: MySQL Not Running
- Make sure MySQL server is running
- Check MySQL service status
- Try: `python setup_mysql.py` to test connection

#### Issue: Port 8000 Already in Use
```bash
# Find what's using port 8000
netstat -ano | findstr :8000

# Or change port in backend/main.py (line 69)
```

### Step 3: Start the Server

**Option 1: From project root**
```bash
python start_server.py
```

**Option 2: From backend directory**
```bash
cd backend
python main.py
```

**Option 3: Using uvicorn directly**
```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Expected Output

When successful, you should see:
```
Initializing database at: mysql+pymysql://root:****@localhost:3306/secure_notes
✅ Database tables created/verified
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

## Common Error Messages

### "ModuleNotFoundError: No module named 'fastapi'"
**Fix:** `pip install -r requirements.txt`

### "ImportError: cannot import name 'Base'"
**Fix:** Clear cache and restart: `rmdir /s /q backend\__pycache__`

### "Can't connect to MySQL server"
**Fix:** 
1. Make sure MySQL is running
2. Check MySQL credentials in `backend/database/database.py`
3. Run `python setup_mysql.py`

### "Address already in use"
**Fix:** 
1. Close other applications using port 8000
2. Or change port in `backend/main.py`

### "Table 'secure_notes.users' doesn't exist"
**Fix:** 
1. Make sure database exists: `python setup_mysql.py`
2. Restart the server (tables are created automatically)

## Still Not Working?

1. **Run the debug script:**
   ```bash
   python debug_backend.py
   ```

2. **Check the error message** - it will tell you exactly what's wrong

3. **Share the error output** from `debug_backend.py` for help

## Verification

Once the server starts:
1. Open browser: `http://localhost:8000`
2. Should see: `{"message":"Secure Notes API is running"}`
3. API docs: `http://localhost:8000/docs`
