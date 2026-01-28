# Troubleshooting Guide

## If you can't copy from terminal, use these tools:

### Option 1: Run Diagnostic Script
```bash
python diagnose.py
```
This will create `error_log.txt` with all the information. Open that file to see what's wrong.

### Option 2: Use the Safe Runner
```bash
run_backend_safe.bat
```
This will show clear error messages and suggestions.

### Option 3: Capture Output to File
```bash
run_and_capture.bat
```
This will save all output to `output.log` file.

## Common Errors and Solutions

### Error: "ModuleNotFoundError: No module named 'fastapi'"
**Solution:**
```bash
pip install -r requirements.txt
```

### Error: "ModuleNotFoundError: No module named 'database'"
**Solution:**
- Make sure you're running from the `backend` directory:
  ```bash
  cd backend
  python main.py
  ```
- OR use the alternative:
  ```bash
  python start_server.py
  ```

### Error: "Address already in use" or Port 8000 error
**Solution:**
- Close other applications using port 8000
- Or change the port in `backend/main.py` line 56

### Error: "ImportError" or "cannot import name"
**Solution:**
1. Make sure all `__init__.py` files exist:
   - `backend/__init__.py`
   - `backend/api/__init__.py`
   - `backend/database/__init__.py`

2. Reinstall packages:
   ```bash
   pip install --upgrade -r requirements.txt
   ```

### Error: "Python is not recognized"
**Solution:**
- Make sure Python is installed
- Add Python to your PATH
- Or use full path: `C:\Python3x\python.exe main.py`

## Quick Check Commands

1. **Check Python version:**
   ```bash
   python --version
   ```
   Should be 3.8 or higher

2. **Check if packages are installed:**
   ```bash
   pip list | findstr fastapi
   pip list | findstr uvicorn
   ```

3. **Check directory structure:**
   ```bash
   dir backend
   dir backend\api
   dir backend\database
   ```

## Still Having Issues?

1. Run `python diagnose.py` and check `error_log.txt`
2. Run `run_backend_safe.bat` and read the error messages
3. Check if all files are in the correct locations
4. Make sure you're using a virtual environment (recommended)
