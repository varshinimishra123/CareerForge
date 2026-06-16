from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.db.database import Base


class Application(Base):
    __tablename__ = "applications"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    company = Column(
        String,
        nullable=False
    )

    role = Column(
        String,
        nullable=False
    )

    status = Column(
        String,
        default="Applied"
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )