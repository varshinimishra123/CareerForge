from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.job import Job

from app.schemas.job import JobCreate

from app.services.job_matcher import (
    extract_job_skills
)

from app.models.resume import Resume

from app.services.job_ats import (
    calculate_job_match_score
)

from app.services.recommender import (
    generate_recommendations
)

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


@router.post("/create")
def create_job(
    job: JobCreate,
    db: Session = Depends(get_db)
):

    skills = extract_job_skills(
        job.description
    )

    new_job = Job(
        title=job.title,
        company=job.company,
        description=job.description,
        skills=",".join(skills)
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return {
        "job_id": new_job.id,
        "title": new_job.title,
        "company": new_job.company,
        "skills": skills
    }


@router.get("/")
def get_jobs(
    db: Session = Depends(get_db)
):

    jobs = db.query(Job).all()

    return jobs


@router.get("/{job_id}")
def get_job(
    job_id: int,
    db: Session = Depends(get_db)
):

    job = (
        db.query(Job)
        .filter(Job.id == job_id)
        .first()
    )

    if not job:
        return {
            "message": "Job not found"
        }

    return job

@router.post("/{job_id}/match")
def match_job(
    job_id: int,
    db: Session = Depends(get_db)
): 
    
    job = (
        db.query(Job)
        .filter(Job.id == job_id)
        .first()
    )

    if not job:
        return {
            "message": "Job not found"
        }

    resume = (
        db.query(Resume)
        .order_by(Resume.id.desc())
        .first()
    )

    if not resume:
        return {
            "message": "Resume not found"
        }

    resume_skills = [
        skill.strip()
        for skill in resume.skills.split(",")
        if skill.strip()
    ]

    job_skills = [
        skill.strip()
        for skill in job.skills.split(",")
        if skill.strip()
    ]

    result = calculate_job_match_score(
        resume_skills,
        job_skills
    )

    recommendations = generate_recommendations(
        result["missing_skills"]
    )

    return {
        "job_id": job.id,
        "job_title": job.title,
        "company": job.company,
        **result,
        "recommendations": recommendations
    }    