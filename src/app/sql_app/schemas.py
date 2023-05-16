from datetime import datetime
import uuid
from pydantic import BaseModel


class LiftBase(BaseModel):
    name: str
    training_max: int


class Lift(LiftBase):
    id: int
    user_id: int
    lift_key: uuid.UUID
    is_active: bool
    is_deleted: bool
    created_date: datetime
    modified_date: datetime

    class Config:
        orm_mode = True


class LiftCreate(BaseModel):
    user_id: int


class UserBase(BaseModel):
    pass


class User(UserBase):
    user_key: uuid.UUID
    email: str
    is_active: bool
    is_deleted: bool
    created_date: datetime
    modified_date: datetime

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    user_email: str
    user_key = uuid.uuid4()
