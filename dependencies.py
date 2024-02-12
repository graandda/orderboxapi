from sqlalchemy.orm import Session
from db import engine


def get_db():
    db = engine.SessionLocal()
    try:
        yield db
    finally:
        db.close()
