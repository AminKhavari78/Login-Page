from pydantic import BaseModel
from typing import Optional, List
class Notification(BaseModel):
    author: str
    description: str


class User(BaseModel):
    name: str
    username: str
    email: str
    birthday: Optional[str] = ""
    friends: Optional[List[str]] = []
    notifications: Optional[List[Notification]] = []


class UserDB(User):
    hashed_password: str