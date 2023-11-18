from fastapi import APIRouter, Body, Depends

from dependencies import admin_service
from services.admin import AdminService
from schemas.admin import Admin, AdminLogin

from dependencies import user_service
from services.user import UserService
from schemas.user import UserRegister

router = APIRouter(prefix="/admin", tags=["admin"])


@router.post("/login")
async def login(
    admin: AdminLogin = Body(),
    admin_service: AdminService = Depends(admin_service)
):
    return await admin_service.login(admin)


@router.post("/register_user")
async def register(
    user: UserRegister = Body(),
    user_service: UserService = Depends(user_service)
):
    return await user_service.register(user)
