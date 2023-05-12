from fastapi import APIRouter, Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.sql_app import schemas
from app.sql_app import crud
from app.sql_app import models
from app.sql_app.database import SessionLocal
from uuid import UUID


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


@router.get("/{user_id}")
async def get_user(user_id: UUID, db: Session = Depends(get_db)):
    user: models.User | None = crud.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
