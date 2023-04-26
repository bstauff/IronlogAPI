from fastapi import APIRouter

from .endpoints import lifts

api_router = APIRouter()
api_router.include_router(lifts.router, prefix="/lifts", tags=["lifts"])
