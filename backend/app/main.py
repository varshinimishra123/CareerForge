from fastapi import FastAPI

from app.db.database import engine
from app.db.database import Base

from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CareerForge API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "CareerForge Backend Running"
    }