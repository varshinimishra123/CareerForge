def calculate_job_match_score(
    resume_skills: list,
    job_skills: list
):

    resume_set = set(
        skill.lower()
        for skill in resume_skills
    )

    job_set = set(
        skill.lower()
        for skill in job_skills
    )

    matched_skills = list(
        resume_set.intersection(job_set)
    )

    missing_skills = list(
        job_set - resume_set
    )

    if len(job_set) == 0:
        score = 0
    else:
        score = round(
            (len(matched_skills) / len(job_set))
            * 100
        )

    return {
        "job_match_score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }