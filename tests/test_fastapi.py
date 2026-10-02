from fastapi.testclient import TestClient

from fraud_detection.fastapi_app.main import app

client = TestClient(app)


# ==========API Integration Testing====================================
def test_predict_endpoint_returns_Not_fraud():

    fake_data = {
        "Time": 0.0,
        "V1": -1.359807,
        "V2": -0.072781,
        "V3": 2.536347,
        "V4": 1.378155,
        "V5": -0.338321,
        "V6": 0.462388,
        "V7": 0.239599,
        "V8": 0.098698,
        "V9": 0.363787,
        "V10": 0.090794,
        "V11": -0.551600,
        "V12": -0.617801,
        "V13": -0.991390,
        "V14": -0.311169,
        "V15": 1.468177,
        "V16": -0.470401,
        "V17": 0.207971,
        "V18": 0.025791,
        "V19": 0.403993,
        "V20": 0.251412,
        "V21": -0.018307,
        "V22": 0.277838,
        "V23": -0.110474,
        "V24": 0.066928,
        "V25": 0.128539,
        "V26": -0.189115,
        "V27": 0.133558,
        "V28": -0.021053,
        "Amount": 149.62,
    }

    response = client.post("/api/v1/fraud-detection/predict", json=fake_data)

    assert response.status_code == 200
    assert response.json()["fraud_status"] == "Not Fraud"


def test_predict_endpoint_returns_fraud():

    fake_data = {
        "Time": 0.0,
        "V1": -1.359807,
        "V2": -0.072781,
        "V3": 2.536347,
        "V4": 1.378155,
        "V5": -0.338321,
        "V6": 0.462388,
        "V40": 0.239599,
        "V50": 0.098698,
        "V60": 0.363787,
        "V70": 0.090794,
        "V11": -0.551600,
        "V12": -0.617801,
        "V13": -0.991390,
        "V14": -0.311169,
        "V15": 1.468177,
        "V16": -0.470401,
        "V17": 0.207971,
        "V18": 0.025791,
        "V19": 0.403993,
        "V20": 0.251412,
        "V21": -0.018307,
        "V22": 0.277838,
        "V23": -0.110474,
        "V24": 0.066928,
        "V25": 0.128539,
        "V26": -0.189115,
        "V27": 0.133558,
        "V28": -0.021053,
        "Amount": 149.62,
    }

    response = client.post("/api/v1/fraud-detection/predict", json=fake_data)

    assert response.status_code == 422  # ====Pydantic catches it=========
