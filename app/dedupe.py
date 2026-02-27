print("LOADING DEDUPE MODULE")
from config import redis_client
import hashlib
import json

DUPLICATE_TTL = 300  # 5 minutes


def generate_event_hash(event):
    event_dict = {
        "user_id": event.user_id,
        "event_type": event.event_type,
        "message": event.message,
        "source": event.source
    }

    event_string = json.dumps(event_dict, sort_keys=True)
    return hashlib.sha256(event_string.encode()).hexdigest()


def is_duplicate(event):
    event_hash = generate_event_hash(event)

    if redis_client.exists(event_hash):
        return True

    redis_client.setex(event_hash, DUPLICATE_TTL, 1)
    return False