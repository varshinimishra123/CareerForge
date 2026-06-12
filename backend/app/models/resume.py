from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime

from datetime import datetime

from app.db.database import Base


class Resume(Base):

    __tablename__ = "resumes"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
    Integer
    )

    filename = Column(
        String,
        nullable=False
    )

    extracted_text = Column(
        Text,
        nullable=False
    )

    skills = Column(
        Text,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )