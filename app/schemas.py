from pydantic import BaseModel
from datetime import date

class UserCreate(BaseModel):
    username: str
    password_hash: str
    role: str
    full_name: str

class UserOut(BaseModel):
    user_id: int
    username: str
    role: str
    full_name: str
    created_at: date

    class Config:
        orm_mode = True

class KeyboxCreate(BaseModel):
    chat_box_id: int
    user_id: int
    
class ChatBoxCreate(BaseModel):
    name: str

class ChatBoxOut(BaseModel):
    chat_box_id: int
    name: str
    created_by: int
    created_at: date

    class Config:
        orm_mode = True

class MessageCreate(BaseModel):
    chat_box_id: int
    content: str

class MessageOut(BaseModel):
    message_id: int
    chat_box_id: int
    sender_id: int
    content: str
    sent_at: date

    class Config:
        orm_mode = True
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class UserLogin(BaseModel):
    username: str
    password: str