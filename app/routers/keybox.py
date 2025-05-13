from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import get_db
from ..oauth2 import get_current_user

router = APIRouter(prefix="/keybox", tags=["Keybox"])

@router.post("/assign")
def assign_keybox_entry(data: schemas.KeyboxCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return crud.assign_key(db, chat_box_id=data.chat_box_id, user_id=data.user_id)
