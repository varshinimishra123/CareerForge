SKILL_RECOMMENDATIONS = {
    "docker": "Learn Docker fundamentals and containerize a FastAPI project.",
    "fastapi": "Build REST APIs using FastAPI and explore dependency injection.",
    "postgresql": "Practice database design, joins, indexing, and SQL queries.",
    "redis": "Learn caching, session storage, and Redis data structures.",
    "aws": "Learn EC2, S3, IAM, and deploy a project on AWS.",
    "react": "Build frontend projects using React hooks and component architecture.",
    "machine learning": "Study supervised learning, feature engineering, and model evaluation.",
    "git": "Practice branching, merging, pull requests, and Git workflows."
}

def generate_recommendations(missing_skills):

    recommendations = []

    for skill in missing_skills:

        skill_lower = skill.lower()

        if skill_lower in SKILL_RECOMMENDATIONS:
            recommendations.append(
                {
                    "skill": skill,
                    "recommendation": SKILL_RECOMMENDATIONS[skill_lower]
                }
            )

    return recommendations