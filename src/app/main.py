from fastapi import FastAPI

from api.api_v1.endpoints import lifts

app = FastAPI()

app.include_router(lifts.router)
