from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.sql_app import schemas
from app.sql_app import crud
from app.sql_app import models
from app.sql_app.database import SessionLocal


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
async def create_user(db: Session = Depends(get_db)):
    new_user = schemas.UserCreate()
    created_user: models.User = crud.create_user(db=db, user=new_user)
    return created_user
