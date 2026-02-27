from fastapi import FastAPI
from schemas import NotificationEvent
from decision_engine import evaluate_notification
app = FastAPI(title="AI Notification Prioritization Engine")

@app.get("/")
def health_check():
    return {"status": "Engine Running"}

@app.post("/evaluate-notification")
def evaluate(event: NotificationEvent):
    decision = evaluate_notification(event)
    return decision