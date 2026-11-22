from datetime import datetime, timezone
from pydantic import BaseModel, Field


class AlertEvent(BaseModel):
    source_video: str = Field(min_length=1)
    event_type: str = Field(min_length=1)
    summary: str
    model_id: str
    review_status: str = "pending"
    timestamp_utc: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
