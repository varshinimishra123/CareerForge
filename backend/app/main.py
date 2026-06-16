from fastapi import FastAPI

from app.db.database import engine
from app.db.database import Base

from app.models.user import User
from app.models.resume import Resume
from app.models.job import Job

from app.api.auth import router as auth_router

from app.api.users import router as users_router
from app.api.resume import router as resume_router
from app.api import jobs
from app.api.dashboard import router as dashboard_router

from fastapi.middleware.cors import CORSMiddleware
from app.api import application

Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="CareerForge API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(resume_router)
app.include_router(jobs.router)
app.include_router(dashboard_router)
app.include_router(
    application.router
)

@app.get("/")
def root():
    return {
        "message": "CareerForge Backend Running"
    }