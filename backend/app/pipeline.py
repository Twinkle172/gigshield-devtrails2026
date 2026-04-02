from .features import build_features
from .model import predict_probability
from .rules import rule_engine
from .scoring import compute_score
from .decision import make_decision
from .database import save_log

def run_pipeline(data):
    features = build_features(data)
    ml_prob = predict_probability(features)
    rule_flags = rule_engine(data)
    fraud_score = compute_score(ml_prob, rule_flags)
    decision = make_decision(fraud_score)

    result = {
        "fraud_score": fraud_score,
        "decision": decision
    }

    save_log({**data, **result})

    return result
