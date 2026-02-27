from datetime import datetime

def log_decision(event, decision_data, fatigue_data=None):

    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "user_id": event.user_id,
        "event_type": event.event_type,
        "decision": decision_data["decision"],
        "explanation": decision_data["explanation"],
        "fatigue_score": fatigue_data["fatigue_score"] if fatigue_data else None
    }

    print("AUDIT LOG:", log_entry)

    return log_entry