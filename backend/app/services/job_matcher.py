from app.core.skills import KNOWN_SKILLS


def extract_job_skills(job_description: str):

    found_skills = []

    job_description = job_description.lower()

    for skill in KNOWN_SKILLS:

        if skill.lower() in job_description:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))


def compare_skills(
    resume_skills,
    job_skills
):

    matched_skills = []
    missing_skills = []

    resume_set = set(resume_skills)

    for skill in job_skills:

        if skill in resume_set:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    if len(job_skills) == 0:
        match_percentage = 0
    else:
        match_percentage = round(
            (len(matched_skills) / len(job_skills)) * 100,
            2
        )

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_percentage": match_percentage
    }