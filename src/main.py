from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.user import router as user_router
from routers.admin import router as admin_router

from db.database import create_tables

app = FastAPI()
main_router = APIRouter(prefix="/api/v1")

origins = ["http://localhost:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)


main_router.include_router(user_router)
main_router.include_router(admin_router)
app.include_router(main_router)