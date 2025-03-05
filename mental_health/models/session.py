from datetime import datetime
import uuid

from pydantic import BaseModel, Field

class _Session_v0(BaseModel):
    created_at: datetime = Field(default_factory=datetime.now)
    uuid: uuid.UUID

Session = _Session_v0
