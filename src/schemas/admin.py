from pydantic import BaseModel


class Admin(BaseModel):
    id: int
    username: str
    password: str
    mail: str


class AdminLogin(BaseModel):
    username: str
    password: str
