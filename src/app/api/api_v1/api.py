from fastapi import APIRouter

from .endpoints import lifts
from .endpoints import users

api_router = APIRouter()
api_router.include_router(lifts.router, prefix="/lifts", tags=["lifts"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
