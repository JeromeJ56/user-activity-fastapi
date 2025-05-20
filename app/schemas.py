from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime


class ActivityBase(BaseModel):
    activity_type: str
    details: str = None

class UserBase(BaseModel):
    username: str
    meta_data: Optional[Dict[str, Any]] = None

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True