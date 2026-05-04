import random

def predict_risk(data):
    # simple mock ML logic
    score = random.uniform(0, 1)

    if score > 0.7:
        risk = "High"
    elif score > 0.4:
        risk = "Medium"
    else:
        risk = "Low"

    return {
        "risk": risk,
        "confidence": round(score, 2)
    }
