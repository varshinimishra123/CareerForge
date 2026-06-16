from typing import List

from pydantic import BaseModel


class InterviewStartRequest(BaseModel):
    role: str


class QuestionResponse(BaseModel):
    id: int
    question: str

    class Config:
        from_attributes = True


class InterviewStartResponse(BaseModel):
    session_id: int
    questions: List[QuestionResponse]


class AnswerSubmission(BaseModel):
    question_id: int
    answer: str


class InterviewSubmitRequest(BaseModel):
    session_id: int
    answers: List[AnswerSubmission]


class EvaluationResult(BaseModel):
    question_id: int
    score: float
    feedback: str
    strengths: str
    improvements: str


class InterviewSubmitResponse(BaseModel):
    overall_score: float
    results: List[EvaluationResult]