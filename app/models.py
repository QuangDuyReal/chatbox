from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "User"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(10), nullable=False)
    full_name = Column(String(100))
    created_at = Column(Date)
    updated_at = Column(Date)

    messages = relationship("Message", back_populates="sender")

class ChatBox(Base):
    __tablename__ = "ChatBoxes"
    chat_box_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    created_by = Column(Integer, ForeignKey("User.user_id"))
    created_at = Column(Date)

class UserChatBox(Base):
    __tablename__ = "UserChatBox"
    user_id = Column(Integer, ForeignKey("User.user_id"), primary_key=True)
    chat_box_id = Column(Integer, ForeignKey("ChatBoxes.chat_box_id"), primary_key=True)

class Message(Base):
    __tablename__ = "Messages"
    message_id = Column(Integer, primary_key=True, index=True)
    chat_box_id = Column(Integer, ForeignKey("ChatBoxes.chat_box_id"))
    sender_id = Column(Integer, ForeignKey("User.user_id"))
    content = Column(Text, nullable=False)
    sent_at = Column(Date)

    sender = relationship("User", back_populates="messages")

class Keybox(Base):
    __tablename__ = "Keybox"
    key_id = Column(Integer, primary_key=True, index=True)
    chat_box_id = Column(Integer, ForeignKey("ChatBoxes.chat_box_id"))
    user_id = Column(Integer, ForeignKey("User.user_id"))
