def get_readiness(score: int):

    if score >= 80:
        return "Ready to Apply"

    if score >= 60:
        return "Almost Ready"

    if score >= 40:
        return "Needs Improvement"

    return "Not Ready"