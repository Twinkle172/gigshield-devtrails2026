def decide(score):
    if score <= 30:
        return "APPROVE"
    elif score <= 60:
        return "REVIEW"
    elif score <= 80:
        return "RESTRICT"
    else:
        return "BLOCK"