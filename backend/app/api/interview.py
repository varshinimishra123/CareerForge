from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.database import get_db
from app.core.dependencies import get_current_user

from app.models.user import User

from app.schemas.interview import (
    InterviewStartRequest,
)

from app.services.interview_service import (
    InterviewService,
)
from app.schemas.interview import (
    InterviewSubmitRequest,
)

router = APIRouter(
    prefix="/interview",
    tags=["Interview"]
)

@router.post("/start")
def start_interview(
    data: InterviewStartRequest,
    db: Session = Depends(get_db),
):

    current_user = {
        "id": 1
    }

    result = InterviewService.create_session(
        db=db,
        user_id=current_user["id"],
        role=data.role,
    )

    return {
        "session_id": result["session"].id,
        "questions": [
            {
                "id": q.id,
                "question": q.question,
            }
            for q in result["questions"]
        ]
    }

@router.post("/submit")
def submit_interview(
    data: InterviewSubmitRequest,
    db: Session = Depends(get_db),
):

    result = InterviewService.submit_answers(
        db=db,
        session_id=data.session_id,
        answers=data.answers,
    )

    return result

@router.get("/history")
def get_interview_history(
    db: Session = Depends(get_db),
):

    current_user = {
        "id": 1
    }

    interviews = InterviewService.get_history(
        db=db,
        user_id=current_user["id"]
    )

    return [
        {
            "id": interview.id,
            "role": interview.role,
            "status": interview.status,
            "overall_score": interview.overall_score,
            "created_at": interview.created_at,
        }
        for interview in interviews
    ] 

@router.get("/{session_id}")
def get_interview_report(
    session_id: int,
    db: Session = Depends(get_db),
):

    report = InterviewService.get_report(
        db=db,
        session_id=session_id,
    )

    return report