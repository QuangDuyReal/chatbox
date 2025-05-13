from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, crud, models
from ..oauth2 import get_db, get_current_user

router = APIRouter(prefix="/chatboxes", tags=["ChatBoxes"])

@router.post("/", response_model=schemas.ChatBoxOut)
def create_chatbox(chatbox: schemas.ChatBoxCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return crud.create_chatbox(db, chatbox, user_id=user.user_id)

@router.get("/", response_model=list[schemas.ChatBoxOut])
def list_chatboxes(db: Session = Depends(get_db), user=Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admins only")
    return db.query(models.ChatBox).all()