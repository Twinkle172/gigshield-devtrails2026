def apply_rules(data):
    score = 0

    if data.get("gps_jitter", 1) == 0:
        score += 20

    if data.get("network_type") == "wifi":
        score += 10

    if data.get("movement") == "static":
        score += 15

    if data.get("ip_mismatch"):
        score += 20

    if data.get("claim_frequency", 0) > 5:
        score += 15

    return score