from config import redis_client
WINDOW_5_MIN = 300
WINDOW_1_HOUR = 3600

MAX_5_MIN = 5
MAX_1_HOUR = 20

def update_and_check_fatigue(user_id: str):
    
    key_5 = f"user:{user_id}:5min"
    key_1h = f"user:{user_id}:1hour"

    # Increment counters
    count_5 = redis_client.incr(key_5)
    count_1h = redis_client.incr(key_1h)

    # Set expiry only if first time
    if count_5 == 1:
        redis_client.expire(key_5, WINDOW_5_MIN)

    if count_1h == 1:
        redis_client.expire(key_1h, WINDOW_1_HOUR)

    fatigue_score = (count_5 / MAX_5_MIN) * 0.6 + (count_1h / MAX_1_HOUR) * 0.4

    return {
        "count_5min": count_5,
        "count_1hour": count_1h,
        "fatigue_score": fatigue_score
    }