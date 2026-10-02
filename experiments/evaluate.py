import json

import joblib
import mlflow
import pandas as pd
from config import load_config
from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score

xgboost_model = joblib.load("models/xgboost_model.pkl")


def evaluate_model():
    cfg = load_config()
    cfg_estimators = cfg["model"]["n_estimators"]
    cfg_depth = cfg["model"]["max_depth"]
    cfg_random_state = cfg["model"]["random_state"]
    cfg_pos_weights = cfg["model"]["scale_pos_weight"]

    val_path = "data/processed/val.parquet"
    df = pd.read_parquet(val_path)

    x_test = df.drop(columns=["Class"])
    y_test = df["Class"]

    y_pred = xgboost_model.predict(x_test)

    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    cm = confusion_matrix(y_test, y_pred)
    print(f"confusion matrix: {cm}")

    my_metrices = {"precision": precision, "recall": recall, "f1_score": f1}

    my_params = {
        "n_estimators": cfg_estimators,
        "max_depth": cfg_depth,
        "random_state": cfg_random_state,
        "scale_pos_weight": cfg_pos_weights,
    }

    metrices_file = "metrices/scores.json"
    with open(metrices_file, "w") as f:
        json.dump(my_metrices, f, indent=4)

    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    mlflow.set_experiment("my-first-experiment")

    # log model && metrices
    with mlflow.start_run(run_name="first-run"):
        mlflow.log_metrics(my_metrices)
        mlflow.log_params(my_params)
        mlflow.xgboost.log_model(xgb_model=xgboost_model, name="XGBoost")


if __name__ == "__main__":
    evaluate_model()
