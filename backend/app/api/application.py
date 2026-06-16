from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.application import Application

from app.schemas.application import (
    ApplicationCreate,
    ApplicationUpdate,
    ApplicationResponse
)
router = APIRouter(
    prefix="/applications",
    tags=["Applications"]
)

@router.post(
    "/",
    response_model=ApplicationResponse
)
def create_application(
    application: ApplicationCreate,
    db: Session = Depends(get_db)
):
    new_application = Application(
        company=application.company,
        role=application.role,
        status="Applied"
    )

    db.add(new_application)
    db.commit()
    db.refresh(new_application)

    return new_application

@router.get(
    "/",
    response_model=list[ApplicationResponse]
)
def get_applications(
    db: Session = Depends(get_db)
):
    applications = (
        db.query(Application)
        .all()
    )

    return applications

@router.put(
    "/{application_id}",
    response_model=ApplicationResponse
)
def update_application(
    application_id: int,
    update: ApplicationUpdate,
    db: Session = Depends(get_db)
):
    application = (
        db.query(Application)
        .filter(
            Application.id == application_id
        )
        .first()
    )

    if not application:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    application.status = update.status

    db.commit()
    db.refresh(application)

    return application