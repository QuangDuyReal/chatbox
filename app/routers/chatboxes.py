from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import get_db
from ..oauth2 import get_current_user

router = APIRouter(prefix="/chatboxes", tags=["ChatBoxes"])

@router.post("/", response_model=schemas.ChatBoxOut)
def create_chatbox(chatbox: schemas.ChatBoxCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return crud.create_chatbox(db, chatbox, user_id=user.user_id)
