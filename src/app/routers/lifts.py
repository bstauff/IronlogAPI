import uuid
from fastapi import APIRouter

router = APIRouter()


@router.get("/api/lifts/{user_id}")
async def get_lifts(user_id: uuid.UUID):
    return get_user_lifts(user_id)


class Lift:
    def __init__(self, id: uuid.UUID, name: str, training_max: int):
        self.__id = id
        self.__name = name
        self.__trainingmax = training_max


def get_user_lifts(user_id: uuid.UUID) -> list[Lift]:
    return [
        Lift(uuid.uuid4(), "Squat", 200),
        Lift(uuid.uuid4(), "Bench", 150),
        Lift(uuid.uuid4(), "Deadlift", 250),
    ]
