from .features import extract_features
from .model import predict
from .rules import apply_rules
from .scoring import compute_score
from .decision import decide
from .database import save_log

def run_pipeline(data):
    features = extract_features(data)

    ml_score = predict(features)
    rule_score = apply_rules(data)

    final_score = compute_score(ml_score, rule_score)

    decision = decide(final_score)

    result = {
        "fraud_score": final_score,
        "decision": decision
    }

    save_log({**data, **result})

    return result