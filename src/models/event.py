import datetime

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base


class EventModel(Base):
    __tablename__ = "event"

    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str] = mapped_column(String(100))
    place: Mapped[str] = mapped_column(String(50))
    time: Mapped[datetime.datetime]
    post: Mapped[str]
    is_done: Mapped[bool]
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

    def __repr__(self):
        return f'{self.id} {self.category} {self.place}' \
               f'{self.time} {self.post} {self.is_done}' \
               f'{self.user_id}'
