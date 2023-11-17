import asyncio

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.user import router as user_router
import uvicorn

from db.database import create_tables

app = FastAPI()
main_router = APIRouter(prefix="/api/v1")

origins = ["127.0.0.1:8000"]

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


def main():
    asyncio.run(create_tables())
    main_router.include_router(user_router)
    app.include_router(main_router)
    uvicorn.run(app=app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
