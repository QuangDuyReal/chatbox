from sqlalchemy.orm import Session
from . import models, schemas

# ChatBox CRUD
def create_chatbox(db: Session, chatbox: schemas.ChatBoxCreate, user_id: int):
    new_box = models.ChatBoxes(
        name=chatbox.name,
        created_by=user_id
    )
    db.add(new_box)
    db.commit()
    db.refresh(new_box)
    return new_box

# Message CRUD
def create_message(db: Session, msg: schemas.MessageCreate, sender_id: int):
    message = models.Messages(
        chat_box_id=msg.chat_box_id,
        sender_id=sender_id,
        content=msg.content
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    return message

# Keybox CRUD
def assign_key(db: Session, chat_box_id: int, user_id: int):
    key_entry = models.Keybox(chat_box_id=chat_box_id, user_id=user_id)
    db.add(key_entry)
    db.commit()
    return key_entry
