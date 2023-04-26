import uuid
from fastapi import APIRouter
from domain.lift import Lift

router = APIRouter()


@router.get("/api/lifts/{user_id}")
async def get_lifts(user_id: uuid.UUID):
    return get_user_lifts(user_id)


def get_user_lifts(user_id: uuid.UUID) -> list[Lift]:
    return [
        Lift(uuid.uuid4(), "Squat", 200),
        Lift(uuid.uuid4(), "Bench", 150),
        Lift(uuid.uuid4(), "Deadlift", 250),
    ]
