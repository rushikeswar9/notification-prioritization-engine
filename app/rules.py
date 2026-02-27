# Simple in-memory rule store (later we can move to DB)

RULES = [
    {
        "name": "Limit promotions per hour",
        "condition": {
            "event_type": "promotion",
            "max_1hour": 3
        },
        "action": "NEVER"
    },
    {
        "name": "Always allow fraud alerts",
        "condition": {
            "event_type": "fraud_alert"
        },
        "action": "NOW"
    }
]
from fatigue import update_and_check_fatigue

def evaluate_rules(event, fatigue_data):

    for rule in RULES:

        condition = rule["condition"]

        # Match event_type
        if "event_type" in condition:
            if event.event_type.lower() != condition["event_type"]:
                continue

        # Max per hour check
        if "max_1hour" in condition:
            if fatigue_data["count_1hour"] > condition["max_1hour"]:
                return {
                    "decision": rule["action"],
                    "explanation": f"Rule triggered: {rule['name']}"
                }

        # If only event_type condition
        if len(condition) == 1:
            return {
                "decision": rule["action"],
                "explanation": f"Rule triggered: {rule['name']}"
            }

    return None