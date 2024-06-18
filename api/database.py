from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from .config import get_settings


sqlite_url = get_settings().DATABASE_URL
engine = create_engine(sqlite_url)

def get_session():
    with Session(engine) as session:
        yield session
