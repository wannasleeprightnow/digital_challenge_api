from fastapi import HTTPException

from models.admin import AdminModel
from schemas.admin import Admin, AdminLogin
from repositories.admin import AdminRepository


class AdminService:
    def __init__(self, admin_repo: AdminRepository):
        self.admin_repo: AdminRepository = admin_repo()
    
    async def login(
        self, admin: AdminLogin
    ) -> Admin:
        admin_from_db = await self.user_repo.select_one_admin(admin.username)
        if not admin_from_db:
            raise HTTPException(
                status_code=400,
                detail="User doesnt exist."
            )
        elif Admin.check_password(
            admin.password, admin_from_db.password
        ):
            return admin_from_db
        else:
            raise HTTPException(
                status_code=400,
                detail="Incorrect username or password."
            )
