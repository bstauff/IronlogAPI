from fastapi import FastAPI

from app.routers import lifts

app = FastAPI()

app.include_router(lifts.router)
