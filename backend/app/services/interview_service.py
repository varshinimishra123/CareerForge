import random
from datetime import datetime

from sqlalchemy.orm import Session

from app.models.interview import (
    InterviewSession,
    InterviewQuestion,
    InterviewAnswer,
)

from app.services.question_bank import QUESTION_BANK


class InterviewService:

    @staticmethod
    def generate_questions(role: str):
        """
        Generate random questions based on selected role.
        """

        role = role.lower()

        if role not in QUESTION_BANK:
            raise ValueError("Invalid role")

        questions = QUESTION_BANK[role]

        return random.sample(
            questions,
            min(10, len(questions))
        )

    @staticmethod
    def create_session(
        db: Session,
        user_id,
        role: str,
    ):
        """
        Create interview session and save questions.
        """

        session = InterviewSession(
            user_id=user_id,
            role=role,
        )

        db.add(session)
        db.commit()
        db.refresh(session)

        questions = InterviewService.generate_questions(role)

        for q in questions:
            db.add(
                InterviewQuestion(
                    session_id=session.id,
                    question=q,
                )
            )

        db.commit()

        saved_questions = (
            db.query(InterviewQuestion)
            .filter(
                InterviewQuestion.session_id == session.id
            )
            .all()
        )

        return {
            "session": session,
            "questions": saved_questions
        }

    @staticmethod
    def evaluate_answer(
        question: str,
        answer: str,
    ):
        """
        Temporary evaluator.
        Replace later with Gemini/OpenAI.
        """

        word_count = len(answer.split())

        if word_count >= 100:
            score = 9

        elif word_count >= 50:
            score = 7

        elif word_count >= 20:
            score = 5

        else:
            score = 2

        return {
            "score": score,
            "feedback": "Answer evaluated successfully.",
            "strengths": "Good attempt.",
            "improvements": "Provide more detailed explanation."
        }

    @staticmethod
    def submit_answers(
        db: Session,
        session_id,
        answers,
    ):
        """
        Save answers and calculate interview score.
        """

        session = (
            db.query(InterviewSession)
            .filter(
                InterviewSession.id == session_id
            )
            .first()
        )

        if not session:
            raise ValueError("Interview session not found")

        total_score = 0
        results = []

        for item in answers:

            question = (
                db.query(InterviewQuestion)
                .filter(
                    InterviewQuestion.id == item.question_id
                )
                .first()
            )

            if not question:
                continue

            evaluation = (
                InterviewService.evaluate_answer(
                    question.question,
                    item.answer
                )
            )

            answer_record = InterviewAnswer(
                question_id=question.id,
                answer=item.answer,
                score=evaluation["score"],
                feedback=evaluation["feedback"],
                strengths=evaluation["strengths"],
                improvements=evaluation["improvements"],
            )

            db.add(answer_record)

            total_score += evaluation["score"]

            results.append({
                "question_id": question.id,
                "score": evaluation["score"],
                "feedback": evaluation["feedback"],
                "strengths": evaluation["strengths"],
                "improvements": evaluation["improvements"],
            })

        db.commit()

        overall_score = 0

        if len(results) > 0:
            overall_score = (
                total_score / len(results)
            ) * 10

        session.status = "completed"
        session.overall_score = overall_score
        session.completed_at = datetime.utcnow()

        db.commit()
        db.refresh(session)

        return {
            "overall_score": round(overall_score, 2),
            "results": results
        }

    @staticmethod
    def get_history(
        db: Session,
        user_id,
    ):
        """
        Get interview history for a user.
        """

        return (
            db.query(InterviewSession)
            .filter(
                InterviewSession.user_id == user_id
            )
            .order_by(
                InterviewSession.created_at.desc()
            )
            .all()
        )

    @staticmethod
    def get_report(
        db: Session,
        session_id,
    ):
        """
        Get detailed interview report.
        """

        session = (
            db.query(InterviewSession)
            .filter(
                InterviewSession.id == session_id
            )
            .first()
        )

        if not session:
            return None

        questions = (
            db.query(InterviewQuestion)
            .filter(
                InterviewQuestion.session_id == session_id
            )
            .all()
        )

        report_questions = []

        for question in questions:

            answer = (
                db.query(InterviewAnswer)
                .filter(
                    InterviewAnswer.question_id == question.id
                )
                .first()
            )

            report_questions.append({
                "question_id": question.id,
                "question": question.question,
                "answer": answer.answer if answer else None,
                "score": answer.score if answer else None,
                "feedback": answer.feedback if answer else None,
                "strengths": answer.strengths if answer else None,
                "improvements": answer.improvements if answer else None,
            })

        return {
            "session_id": session.id,
            "role": session.role,
            "status": session.status,
            "overall_score": session.overall_score,
            "created_at": session.created_at,
            "completed_at": session.completed_at,
            "questions": report_questions,
        }