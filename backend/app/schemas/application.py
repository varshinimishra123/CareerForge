from pydantic import BaseModel


class ApplicationCreate(BaseModel):
    company: str
    role: str

class ApplicationUpdate(BaseModel):
    status: str


class ApplicationResponse(BaseModel):
    id: int
    company: str
    role: str
    status: str

    class Config:
        from_attributes = True