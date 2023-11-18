import bcrypt
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base


class UserModel(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str] = mapped_column(String(25))
    name: Mapped[str] = mapped_column(String(25))
    surname: Mapped[str] = mapped_column(String(25))
    name_by_father: Mapped[str] = mapped_column(String(25))
    on_work: Mapped[bool] = mapped_column(default=False)
    job_title: Mapped[str]
    phone_number: Mapped[str] = mapped_column(unique=True)

    @staticmethod
    def hash_password(unhashed_password: str):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(unhashed_password.encode("utf-8"), salt)

    @staticmethod
    def check_password(first_password, second_password):
        return bcrypt.checkpw(
            first_password.encode("utf-8"),
            second_password,
            )

    def __repr__(self):
        return f"{self.id} {self.username} {self.password} \
            {self.name} {self.surname} {self.name_by_father} \
                {self.on_work} {self.job_title} {self.phone_number}"
