@echo off
echo ========================================
echo Checking for errors...
echo ========================================
echo.

REM Run diagnostic
python diagnose.py

echo.
echo ========================================
echo Diagnostic complete!
echo ========================================
echo.
echo Check these files:
echo - error_log.txt (full diagnostic report)
echo - output.log (if you ran the server)
echo.
pause
