from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..oauth2 import get_db
from ..oauth2 import get_current_user

router = APIRouter(prefix="/messages", tags=["Messages"])

@router.post("/", response_model=schemas.MessageOut)
def send_message(msg: schemas.MessageCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return crud.create_message(db, msg, sender_id=user.user_id)
