# import asyncio, datetime
# from sqlalchemy import String, ForeignKey
# from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

PATH_TO_DB = "db.sqlite"


class Base(DeclarativeBase):
    pass


async_engine = create_async_engine(
    f"sqlite+aiosqlite:///{PATH_TO_DB}",
    echo=True,
)

async_session_maker = async_sessionmaker(
    async_engine,
)


# class AdminModel(Base):
#     __tablename__ = "admin"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     username: Mapped[str] = mapped_column(String(50), unique=True)
#     password: Mapped[str] = mapped_column(String(25))
#     mail: Mapped[str]


# class EventModel(Base):
#     __tablename__ = "event"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     category: Mapped[str] = mapped_column(String(100))
#     place: Mapped[str] = mapped_column(String(50))
#     time: Mapped[datetime.datetime]
#     post: Mapped[str] = mapped_column(String(50))
#     is_done: Mapped[bool]
#     user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))


# class UserModel(Base):
#     __tablename__ = "user"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     username: Mapped[str] = mapped_column(String(50), unique=True)
#     password: Mapped[str] = mapped_column(String(25))
#     name: Mapped[str] = mapped_column(String(25))
#     surname: Mapped[str] = mapped_column(String(25))
#     name_by_father: Mapped[str] = mapped_column(String(25))
#     on_work: Mapped[bool] = mapped_column(default_server=False)
#     job_title: Mapped[str]
#     phone_number: Mapped[str] = mapped_column(unique=True)


# class UserEventModel(Base):
#     __tablename__ = "user_event"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     user_id: Mapped[int]
#     event_id: Mapped[int]


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# asyncio.run(create_tables())
