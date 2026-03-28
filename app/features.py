import numpy as np

def extract_features(data):
    return np.array([
        data.get("gps_jitter", 0),
        data.get("speed", 0),
        data.get("network_stability", 0),
        data.get("sensor_variation", 0),
        data.get("claim_frequency", 0)
    ]).reshape(1, -1)