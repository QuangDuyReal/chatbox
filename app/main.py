from fastapi import FastAPI 
from app.databases import Base, engine 
from app.routers import users, messages, chatboxes, keybox

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Chat App API",
    description="Hệ thống phòng chat có phân quyền và bảo mật.",
    version="1.0.0"
)

# Include all routers
app.include_router(users.router)
app.include_router(messages.router)
app.include_router(chatboxes.router)
app.include_router(keybox.router)
