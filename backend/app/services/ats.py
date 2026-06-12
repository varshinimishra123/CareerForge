def calculate_ats_score(
    text: str,
    skills: list
):

    score = 0

    text_lower = text.lower()

    # Skills Section (40 points)

    skill_score = min(len(skills) * 2.5, 40)
    score += skill_score

    # Education Section (15 points)

    education_keywords = [
        "education",
        "cgpa",
        "bachelor",
        "university",
        "college"
    ]

    if any(
        keyword in text_lower
        for keyword in education_keywords
    ):
        score += 15

    # Projects Section (25 points)

    project_keywords = [
        "project",
        "projects",
        "developed",
        "built"
    ]

    if any(
        keyword in text_lower
        for keyword in project_keywords
    ):
        score += 25

    # Experience Section (10 points)

    experience_keywords = [
        "internship",
        "experience",
        "worked",
        "research"
    ]

    if any(
        keyword in text_lower
        for keyword in experience_keywords
    ):
        score += 10

    # Contact Information (10 points)

    has_email = "@" in text

    has_phone = any(
        char.isdigit()
        for char in text
    )

    if has_email and has_phone:
        score += 10

    return min(round(score), 100)