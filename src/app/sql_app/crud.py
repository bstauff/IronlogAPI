from sqlalchemy.orm import Session

from . import models, schemas

import uuid


def get_user(db: Session, user_key: uuid.UUID) -> models.User | None:
    users = db.query(models.User).filter(models.User.user_key == user_key)
    return users.first()


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    db_user: models.User = models.User(user_key=uuid.uuid4())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
