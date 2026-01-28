@echo off
echo ========================================
echo Secure Notes Backend Server
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

echo Python found!
python --version
echo.

REM Check if we're in the right directory
if not exist "backend\main.py" (
    echo ERROR: backend\main.py not found
    echo Please run this script from the project root directory
    pause
    exit /b 1
)

echo Starting server...
echo Server will be available at: http://localhost:8000
echo Press Ctrl+C to stop the server
echo.
echo ========================================
echo.

cd backend
python main.py

if errorlevel 1 (
    echo.
    echo ========================================
    echo ERROR: Server failed to start
    echo ========================================
    echo.
    echo Common issues:
    echo 1. Missing packages - Run: pip install -r requirements.txt
    echo 2. Port 8000 in use - Close other applications
    echo 3. Import errors - Check error message above
    echo.
    pause
)
