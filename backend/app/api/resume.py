import os
import shutil
import fitz  # PyMuPDF

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.resume import Resume

from app.schemas.job import JobMatchRequest

from app.services.skill_extractor import extract_skills
from app.services.job_matcher import extract_job_skills
from app.services.job_ats import calculate_job_match_score
from app.services.recommender import generate_recommendations
from app.services.ats import calculate_ats_score

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    try:
        document = fitz.open(
            file_path
        )

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to process PDF: {str(e)}"
        )

    skills = extract_skills(
        text
    )

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
        raise HTTPException(
            status_code=404,
            detail="No resume found"
        )

    resume_skills = [
        skill.strip()
        for skill in latest_resume.skills.split(",")
        if skill.strip()
    ]

    job_skills = extract_job_skills(
        request.job_description
    )

    job_analysis = calculate_job_match_score(
        resume_skills,
        job_skills
    )

    recommendations = generate_recommendations(
        job_analysis["missing_skills"]
    )

    return {
        "resume_id": latest_resume.id,
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        **job_analysis,
        "recommendations": recommendations
    }


@router.get("/analyze")
def analyze_resume(
    db: Session = Depends(get_db)
):

    latest_resume = (
        db.query(Resume)
        .order_by(Resume.id.desc())
        .first()
    )

    if not latest_resume:
        raise HTTPException(
            status_code=404,
            detail="No resume found"
        )

    resume_skills = [
        skill.strip()
        for skill in latest_resume.skills.split(",")
        if skill.strip()
    ]

    analysis = calculate_ats_score(
        latest_resume.extracted_text,
        resume_skills
    )

    return {
        "resume_id": latest_resume.id,
        "filename": latest_resume.filename,
        "skills": resume_skills,
        **analysis
    }