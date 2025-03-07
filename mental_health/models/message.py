from datetime import datetime
import uuid

from pydantic import BaseModel, Field

BOT_USER_ID = uuid.UUID('00000000-0000-0000-0000-000000000000')

class _Message_v0(BaseModel):
    created_at: datetime = Field(default_factory=datetime.now)
    user_id: uuid.UUID
    content: str|bytes  # Encrypted if FeatureFlags.is_message_encryption_enabled()
    session_id: uuid.UUID
    is_read: bool = True

Message = _Message_v0
