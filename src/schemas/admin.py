from pydantic import BaseModel, validator, EmailStr


class Admin(BaseModel):
    id: int
    username: str
    password: str
    mail: EmailStr


class AdminLogin(BaseModel):
    username: str
    password: str
