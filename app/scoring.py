def compute_score(ml_score, rule_score):
    ml_part = (1 - ml_score) * 50
    total = ml_part + rule_score
    return min(100, max(0, int(total)))