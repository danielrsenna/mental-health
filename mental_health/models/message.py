from datetime import date, datetime, time, timedelta
import uuid

from pydantic import BaseModel, Field

class _Message_v0(BaseModel):
    created_at: datetime = Field(default_factory=datetime.now)
    user_id: uuid.UUID
    content: str
    session_id: uuid.UUID
    is_read: bool = True
    prompt_id: uuid.UUID


Message = _Message_v0
