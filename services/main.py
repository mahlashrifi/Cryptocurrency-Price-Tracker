from fastapi import FastAPI
from peyk import router as peyk_router

app = FastAPI()

app.include_router(peyk_router, prefix="/peyk")
