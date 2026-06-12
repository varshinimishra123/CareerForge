from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.database import get_db

from app.models.resume import Resume
from app.models.user import User

from app.core.dependencies import get_current_user
from app.services.skill_extractor import extract_skills

from app.schemas.job import JobMatchRequest

from app.services.job_matcher import (
    extract_job_skills,
    compare_skills
)

import os
import shutil
import fitz

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

UPLOAD_DIR = "uploads"


@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
   
):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    document = fitz.open(file_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    skills = extract_skills(text)

    resume = Resume(
        user_id=1,
        filename=file.filename,
        extracted_text=text,
        skills=",".join(skills)
    )

    db.add(resume)
    db.commit()
    db.refresh(resume)

    return {
        "resume_id": resume.id,
        "user_id": 1,
        "filename": file.filename,
        "skills": skills
    }
@router.post("/match")
def match_resume_to_job(
    request: JobMatchRequest,
    db: Session = Depends(get_db)
):

    latest_resume = (
        db.query(Resume)
        .order_by(Resume.id.desc())
        .first()
    )

    if not latest_resume:
        return {
            "message": "No resume found"
        }

    resume_skills = latest_resume.skills.split(",")

    job_skills = extract_job_skills(
        request.job_description
    )

    result = compare_skills(
        resume_skills,
        job_skills
    )

    return {
        "resume_id": latest_resume.id,
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        **result
    }