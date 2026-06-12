from fastapi import FastAPI

from app.db.database import engine
from app.db.database import Base

from app.models.user import User

from app.api.auth import router as auth_router

from app.api.users import router as users_router
from app.api.resume import router as resume_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CareerForge API",
    version="1.0.0"
)

app.include_router(auth_router)

app.include_router(users_router)

app.include_router(resume_router)

@app.get("/")
def root():
    return {
        "message": "CareerForge Backend Running"
    }