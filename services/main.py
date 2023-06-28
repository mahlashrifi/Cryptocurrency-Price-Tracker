from fastapi import FastAPI
from peyk import router as peyk_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"]
)

app.include_router(peyk_router, prefix="/peyk")
