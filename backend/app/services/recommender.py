SKILL_RECOMMENDATIONS = {
    "Docker": "Learn Docker fundamentals and containerize a FastAPI project.",
    "FastAPI": "Build REST APIs using FastAPI and explore dependency injection.",
    "PostgreSQL": "Practice database design, joins, indexing, and SQL queries.",
    "Redis": "Learn caching, session storage, and Redis data structures.",
    "AWS": "Learn EC2, S3, IAM, and deploy a project on AWS.",
    "React": "Build frontend projects using React hooks and component architecture.",
    "Machine Learning": "Study supervised learning, feature engineering, and model evaluation.",
    "Git": "Practice branching, merging, pull requests, and Git workflows."
}


def generate_recommendations(missing_skills):

    recommendations = []

    for skill in missing_skills:

        if skill in SKILL_RECOMMENDATIONS:
            recommendations.append(
                {
                    "skill": skill,
                    "recommendation": SKILL_RECOMMENDATIONS[skill]
                }
            )

    return recommendations