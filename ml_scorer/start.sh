#!/bin/sh
if [ ! -f "waf_model.pkl" ]; then
    echo "[INFO] Model not found. Training..."
    python train.py
fi
exec uvicorn service:app --host 0.0.0.0 --port 8000