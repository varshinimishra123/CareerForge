from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    Text,
    Float,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from app.db.database import Base
from sqlalchemy import Integer

class InterviewSession(Base):
    __tablename__ = "interview_sessions"

    id = Column(
    Integer,
    primary_key=True,
    index=True,
    )

    user_id = Column(
    Integer,
    ForeignKey("users.id"),
    nullable=False,
    )

    role = Column(String(50), nullable=False)

    status = Column(
        String(20),
        default="in_progress",
        nullable=False,
    )

    overall_score = Column(Float, nullable=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )

    completed_at = Column(
        DateTime,
        nullable=True,
    )

    questions = relationship(
        "InterviewQuestion",
        back_populates="session",
        cascade="all, delete-orphan",
    )

class InterviewQuestion(Base):
        __tablename__ = "interview_questions"

        id = Column(
        Integer,
        primary_key=True,
        index=True,
        )

        session_id = Column(
            Integer,
            ForeignKey("interview_sessions.id"),
        )

        question = Column(Text, nullable=False)

        difficulty = Column(
            String(20),
            nullable=True,
        )

        category = Column(
            String(50),
            nullable=True,
        )

        session = relationship(
            "InterviewSession",
            back_populates="questions",
        )

        answers = relationship(
            "InterviewAnswer",
            back_populates="question_ref",
            cascade="all, delete-orphan",
        )

class InterviewAnswer(Base):
        __tablename__ = "interview_answers"

        id = Column(
        Integer,
        primary_key=True,
        index=True,
        )

        question_id = Column(
        Integer,
        ForeignKey("interview_questions.id"),
        )

        answer = Column(Text, nullable=False)

        score = Column(Float)

        feedback = Column(Text)

        strengths = Column(Text)

        improvements = Column(Text)

        question_ref = relationship(
            "InterviewQuestion",
            back_populates="answers",
        )