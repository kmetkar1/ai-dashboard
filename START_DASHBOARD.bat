@echo off
echo ============================================================
echo    AI Implementation Dashboard Server
echo ============================================================
echo.
echo Starting local server on port 8000...
echo.
echo Dashboard will open at: http://localhost:8000/dashboard.html
echo.
echo Press Ctrl+C to stop the server
echo ============================================================
echo.

cd /d "%~dp0"
start http://localhost:8000/dashboard.html
python -m http.server 8000

pause

@REM Made with Bob
