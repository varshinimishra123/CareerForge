from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.resume import Resume
from app.models.job import Job

from app.services.ats import calculate_ats_score
from app.services.job_ats import calculate_job_match_score

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/")
def get_dashboard(
    db: Session = Depends(get_db)
):

    resume = (
        db.query(Resume)
        .order_by(Resume.id.desc())
        .first()
    )

    if not resume:
        return {
            "message": "No resume found"
        }

    resume_skills = [
        skill.strip()
        for skill in resume.skills.split(",")
        if skill.strip()
    ]

    ats_analysis = calculate_ats_score(
        resume.extracted_text,
        resume_skills
    )

    jobs = db.query(Job).all()

    best_score = 0
    best_job = None

    all_missing_skills = []

    for job in jobs:

        job_skills = [
            skill.strip()
            for skill in job.skills.split(",")
            if skill.strip()
        ]

        result = calculate_job_match_score(
            resume_skills,
            job_skills
        )

        all_missing_skills.extend(
            result["missing_skills"]
        )

        if result["job_match_score"] > best_score:
            best_score = result["job_match_score"]
            best_job = job

    return {
        "resume_id": resume.id,
        "ats_score": ats_analysis["ats_score"],
        "total_jobs": len(jobs),
        "best_match_score": best_score,
        "best_matching_job": (
            best_job.title
            if best_job
            else None
        ),
        "top_missing_skills": list(
            set(all_missing_skills)
        )[:5]
    }