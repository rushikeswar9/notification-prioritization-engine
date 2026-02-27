# Notification Prioritization Engine

An AI-driven notification decision engine built using FastAPI and Redis.

## Features
- Exact duplicate detection using Redis hashing
- Sliding window alert fatigue detection
- Configurable rule engine
- Context-aware priority boosting
- Explainability logging for audit tracking

## Tech Stack
- Python
- FastAPI
- Redis

## Run Locally
cd app
python -m uvicorn main:app
