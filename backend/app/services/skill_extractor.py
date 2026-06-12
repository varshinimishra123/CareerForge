KNOWN_SKILLS = [
    "Python",
    "Java",
    "C++",
    "C",
    "JavaScript",
    "HTML",
    "CSS",
    "SQL",
    "Git",
    "GitHub",
    "FastAPI",
    "React",
    "Node.js",
    "MongoDB",
    "PostgreSQL",
    "Machine Learning",
    "Data Structures",
    "Algorithms"
]


def extract_skills(text: str):

    found_skills = []

    text_lower = text.lower()

    for skill in KNOWN_SKILLS:

        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills