from repositories.admin import AdminRepository
from repositories.event import EventRepository
from repositories.user import UserRepository
from services.admin import AdminService
from services.event import EventService
from services.user import UserService


def admin_service():
    return AdminService(AdminRepository)


def event_service():
    return EventService(EventRepository)


def user_service():
    return UserService(UserRepository)
