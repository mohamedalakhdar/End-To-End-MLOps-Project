import joblib
import pandas as pd
from config import load_config
from xgboost import XGBClassifier


def train_model():

    cfg = load_config()
    cfg_estimators = cfg["model"]["n_estimators"]
    cfg_depth = cfg["model"]["max_depth"]
    cfg_random_state = cfg["model"]["random_state"]
    cfg_pos_weights = cfg["model"]["scale_pos_weight"]

    train_path = "data/processed/train.parquet"
    df = pd.read_parquet(train_path)

    x_train = df.drop(columns=["Class"])
    y_train = df["Class"]

    model = XGBClassifier(
        n_estimators=cfg_estimators,
        max_depth=cfg_depth,
        random_state=cfg_random_state,
        scale_pos_weight=cfg_pos_weights,
    )

    # Training
    model.fit(
        x_train,
        y_train,
    )

    model_output_path = "models/xgboost_model.pkl"

    joblib.dump(model, model_output_path)

    print(f"model saved succesusfully: {model_output_path}")


if __name__ == "__main__":
    train_model()
