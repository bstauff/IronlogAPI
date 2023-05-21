from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from . import models, schemas

import uuid


class UserEmailAlreadyExists(Exception):
    pass


def get_user(db: Session, user_key: uuid.UUID) -> models.User | None:
    users = db.query(models.User).filter(models.User.user_key == user_key)
    return users.first()


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    try:
        db_user: models.User = models.User(user_key=uuid.uuid4(), email=user.email)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        raise UserEmailAlreadyExists()
