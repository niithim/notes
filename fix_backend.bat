@echo off
echo ========================================
echo Backend Fix Script
echo ========================================
echo.

REM Step 1: Check Python
echo [1] Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)
python --version
echo.

REM Step 2: Install/Upgrade packages
echo [2] Installing/Upgrading packages...
pip install --upgrade -r requirements.txt
if errorlevel 1 (
    echo WARNING: Some packages may have failed to install
)
echo.

REM Step 3: Clear Python cache
echo [3] Clearing Python cache...
if exist backend\__pycache__ rmdir /s /q backend\__pycache__
if exist backend\api\__pycache__ rmdir /s /q backend\api\__pycache__
if exist backend\database\__pycache__ rmdir /s /q backend\database\__pycache__
echo Cache cleared
echo.

REM Step 4: Run diagnostic
echo [4] Running diagnostic...
python debug_backend.py
echo.

echo ========================================
echo Fix script completed
echo ========================================
echo.
echo If no errors were found, try starting the server:
echo    python start_server.py
echo.
pause
