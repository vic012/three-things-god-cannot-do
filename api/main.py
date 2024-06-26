from fastapi import Depends, FastAPI
from dependencies import get_token_header
from config import get_settings
from routers import views
from internal import admin
from database import engine

# Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mensagens inspiradoras",
    description="Esta API permite o gerenciamento de mensagens inspiradoras",
    version="0.0.1",
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(views.router)
app.include_router(admin.router)
