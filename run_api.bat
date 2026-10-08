@echo off
echo ===================================================
echo RetainIQ - FastAPI Backend Server
echo API will be accessible at: http://localhost:8000
echo OpenAPI Documentation at: http://localhost:8000/docs
echo ===================================================
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
pause
