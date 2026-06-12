from app.core.skills import KNOWN_SKILLS


def extract_skills(text: str):

    found_skills = []

    text_lower = text.lower()

    for skill in KNOWN_SKILLS:

        if skill.lower() in text_lower:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))