#!/usr/bin/env bash
# RetainIQ - Master Launch Script for Linux / macOS
set -e

echo "==================================================="
echo "RetainIQ - Master Orchestrator"
echo "==================================================="

echo "[1/3] Running Automated Tests..."
python -m pytest tests/ -v

echo "[2/3] Pipeline Verification..."
python main.py --stage all

echo "[3/3] Ready to Launch!"
echo "To start FastAPI backend:  uvicorn api.main:app --host 0.0.0.0 --port 8000"
echo "To start Dashboard:        streamlit run app/streamlit_app.py"
