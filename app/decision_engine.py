from schemas import NotificationEvent
from dedupe import is_duplicate
from fatigue import update_and_check_fatigue
from rules import evaluate_rules
from logger import log_decision

def evaluate_notification(event: NotificationEvent):

    # 1️⃣ Duplicate
    if is_duplicate(event):
        result = {
            "decision": "NEVER",
            "explanation": "Duplicate notification detected"
        }
        log_decision(event, result)
        return result

    # 2️⃣ Fatigue
    fatigue_data = update_and_check_fatigue(event.user_id)

    # 3️⃣ Rules
    rule_result = evaluate_rules(event, fatigue_data)
    if rule_result:
        log_decision(event, rule_result, fatigue_data)
        return rule_result

    # 4️⃣ Fatigue suppression
    if fatigue_data["fatigue_score"] > 1 and event.priority_hint < 0.5:
        result = {
            "decision": "NEVER",
            "explanation": "Suppressed due to alert fatigue"
        }
        log_decision(event, result, fatigue_data)
        return result

    # 5️⃣ High priority
    if event.priority_hint and event.priority_hint > 0.7:
        result = {
            "decision": "NOW",
            "explanation": "High priority event"
        }
        log_decision(event, result, fatigue_data)
        return result

    # 6️⃣ Default
    result = {
        "decision": "LATER",
        "explanation": "Scheduled by default logic"
    }

    log_decision(event, result, fatigue_data)
    return result