import joblib
from fastapi import APIRouter

from ..helpers.config import get_settings
from ..models.fraud_model import FraudDectModel
from ..schemas.fraud_schemas import PredictRequest, PredictResponse

fraud_router = APIRouter(
    prefix="/api/v1/fraud-detection",
    tags=["Fraud Detection Model"],
)

settings = get_settings()


xgboost_model = joblib.load(settings.MODEL_PATH)  ## model loaded once

fraud_model = FraudDectModel(model=xgboost_model)


@fraud_router.post("/predict", response_model=PredictResponse)
def fraud_detection_predict(data: PredictRequest, fraud_model=fraud_model):

    model_predection = fraud_model.predict(data=data)
    return PredictResponse(fraud_status=model_predection)
