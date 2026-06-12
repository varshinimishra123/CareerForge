from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from app.services.skill_extractor import extract_skills

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
    file: UploadFile = File(...)
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

    return {
        "filename": file.filename,
        "skills": skills
    }