from pydantic import BaseModel


class JobMatchRequest(BaseModel):
    job_description: str


class JobCreate(BaseModel):
    title: str
    company: str
    description: str