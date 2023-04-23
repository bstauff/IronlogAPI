from fastapi import FastAPI

from routers import lifts

app = FastAPI()

app.include_router(lifts.router)
