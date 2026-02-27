from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class NotificationEvent(BaseModel):
    user_id: str
    event_type: str
    message: str
    source: Optional[str] = None
    priority_hint: Optional[float] = 0.5
    channel: str
    timestamp: datetime
    expires_at: Optional[datetime] = None
    dedupe_key: Optional[str] = None