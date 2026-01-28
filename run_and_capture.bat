@echo off
echo Running backend and capturing output...
echo.
cd backend
python main.py > ..\output.log 2>&1
if errorlevel 1 (
    echo.
    echo ========================================
    echo ERROR OCCURRED
    echo ========================================
    echo Check output.log file in the project root
    type ..\output.log
    echo.
    pause
) else (
    echo.
    echo Server stopped normally
    pause
)
