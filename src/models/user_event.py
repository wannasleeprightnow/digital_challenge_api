from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base


class UserEventModel(Base):
    __tablename__ = "user_event"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    event_id: Mapped[int]

    def __repr__(self):
        return f"{self.id} {self.user_id} {self.event_id}"
