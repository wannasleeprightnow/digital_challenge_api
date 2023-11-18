from repositories.admin import AdminRepository
from repositories.user import UserRepository
from services.admin import AdminService
from services.user import UserService


def admin_service():
    return AdminService(AdminRepository)


def user_service():
    return UserService(UserRepository)
