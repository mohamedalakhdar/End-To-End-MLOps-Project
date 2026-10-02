from pydantic import BaseModel


class PredictRequest(BaseModel):
    # features_name= ["Time"] + [f"V{i}"for i in range(1,29)] + ["Amount"]
    # for field in features_name:
    #     print(f"{field}: float")

    """ "
    schema for validating incoming API request features for fraud detection.
    this docstring will appear directly in your FastAPI Swagger documentation.
    """

    Time: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float


class PredictResponse(BaseModel):
    fraud_status: str
