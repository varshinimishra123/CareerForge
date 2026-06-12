def calculate_ats_score(
    text: str,
    skills: list
):

    score = 0
    strengths = []
    weaknesses = []

    text_lower = text.lower()

    # -------------------------
    # Contact Information (10)
    # -------------------------

    has_email = "@" in text

    has_phone = any(
        char.isdigit()
        for char in text
    )

    if has_email:
        score += 5

    if has_phone:
        score += 5

    if has_email and has_phone:
        strengths.append(
            "Contact information present"
        )
    else:
        weaknesses.append(
            "Missing contact information"
        )

    # -------------------------
    # Education (15)
    # -------------------------

    education_keywords = [
        "education",
        "bachelor",
        "college",
        "university",
        "cgpa"
    ]

    education_matches = sum(
        1 for keyword in education_keywords
        if keyword in text_lower
    )

    education_score = min(
        education_matches * 3,
        15
    )

    score += education_score

    if education_score >= 10:
        strengths.append(
            "Education section is present"
        )
    else:
        weaknesses.append(
            "Education section needs improvement"
        )

    # -------------------------
    # Skills (25)
    # -------------------------

    skill_score = min(
        len(skills),
        25
    )

    score += skill_score

    if len(skills) >= 10:
        strengths.append(
            "Strong skill coverage"
        )
    else:
        weaknesses.append(
            "Add more relevant skills"
        )

    # -------------------------
    # Projects (20)
    # -------------------------

    project_keywords = [
        "project",
        "projects",
        "developed",
        "built",
        "implemented",
        "created"
    ]

    project_matches = sum(
        1 for keyword in project_keywords
        if keyword in text_lower
    )

    project_score = min(
        project_matches * 4,
        20
    )

    score += project_score

    if project_score >= 12:
        strengths.append(
            "Good project experience"
        )
    else:
        weaknesses.append(
            "Add stronger project descriptions"
        )

    # -------------------------
    # Experience (15)
    # -------------------------

    experience_keywords = [
        "internship",
        "experience",
        "worked",
        "research",
        "developer"
    ]

    experience_matches = sum(
        1 for keyword in experience_keywords
        if keyword in text_lower
    )

    experience_score = min(
        experience_matches * 3,
        15
    )

    score += experience_score

    if experience_score >= 9:
        strengths.append(
            "Experience section detected"
        )
    else:
        weaknesses.append(
            "Gain internship or practical experience"
        )

    # -------------------------
    # GitHub & LinkedIn (5)
    # -------------------------

    social_score = 0

    if "github" in text_lower:
        social_score += 3

    if "linkedin" in text_lower:
        social_score += 2

    score += social_score

    if social_score == 5:
        strengths.append(
            "Professional profiles included"
        )
    else:
        weaknesses.append(
            "Add GitHub and LinkedIn links"
        )

    # -------------------------
    # Achievements (10)
    # -------------------------

    achievement_keywords = [
        "achievement",
        "award",
        "winner",
        "rank",
        "certification",
        "certified"
    ]

    achievement_matches = sum(
        1 for keyword in achievement_keywords
        if keyword in text_lower
    )

    achievement_score = min(
        achievement_matches * 2,
        10
    )

    score += achievement_score

    if achievement_score >= 4:
        strengths.append(
            "Achievements detected"
        )
    else:
        weaknesses.append(
            "Add achievements or certifications"
        )

    return {
        "ats_score": min(score, 100),
        "strengths": strengths,
        "weaknesses": weaknesses
    }