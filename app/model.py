from sklearn.ensemble import IsolationForest
import numpy as np

model = IsolationForest(contamination=0.1)

# dummy training (replace later)
model.fit(np.random.rand(100, 5))

def predict(features):
    score = model.decision_function(features)[0]
    return float(score)