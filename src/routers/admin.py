from fastapi import APIRouter, Body, Depends
from fastapi.responses import HTMLResponse

from dependencies import admin_service
from services.admin import AdminService
from schemas.admin import Admin, AdminLogin

router = APIRouter(prefix="/admin", tags=["admin"])

@router.post("/login")
async def login(
    admin: AdminLogin = Body(),
    admin_service: AdminService = Depends(admin_service)
):
    return await admin_service.login(admin)
