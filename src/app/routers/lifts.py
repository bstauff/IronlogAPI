from fastapi import APIRouter

router = APIRouter()


@router.get("/api/lifts")
async def get_lifts():
    return [{"name": "bench press", "weight": 100, "reps": 10}]
