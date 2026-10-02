import pandas as pd

from .base_model import BaseMLModel


class FraudDectModel(BaseMLModel):
    """
    class for loading and running the XGBoost fraud detection model.
    """

    def __init__(self, model):
        self._model = model

    def predict(self, data):
        df = pd.DataFrame([data.model_dump()])
        output = self._model.predict(df)
        class_prediction = output[0]

        def get_fraud_status(class_prediction):
            if class_prediction == 0:
                return "Not Fraud"
            else:
                return "Fraud"

        return get_fraud_status(class_prediction=class_prediction)
