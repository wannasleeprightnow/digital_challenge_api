import asyncio

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.user import router as user_router
from routers.admin import router as admin_router
from routers.event import router as event_router

from db.database import create_tables

app = FastAPI()
main_router = APIRouter(prefix="/api/v1")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

main_router.include_router(user_router)
main_router.include_router(admin_router)
main_router.include_router(event_router)
app.include_router(main_router)
