from fastapi import FastAPI

from src.app.routers import lifts

app = FastAPI()

app.include_router(lifts.router)
