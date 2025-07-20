from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .session import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()