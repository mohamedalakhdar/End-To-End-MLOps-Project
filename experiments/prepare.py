from pathlib import Path

import pandas as pd
from config import load_config
from sklearn.model_selection import train_test_split


def main() -> None:
    cfg = load_config()
    data_cfg = cfg["data"]

    df_full = pd.read_csv(data_cfg["raw_path"])
    df_0 = df_full[df_full["Class"] == 0].sample(
        n=35_000, random_state=42, ignore_index=True
    )
    df_1 = df_full[df_full["Class"] == 1]
    df = pd.concat([df_0, df_1], ignore_index=True)
    df.drop_duplicates(ignore_index=True, inplace=True)
    df.dropna(ignore_index=True, inplace=True)

    train_df, val_df = train_test_split(
        df,
        test_size=data_cfg["test_size"],
        random_state=data_cfg["seed"],
    )

    out_dir = Path("data/processed")
    out_dir.mkdir(parents=True, exist_ok=True)
    train_df.to_parquet(out_dir / "train.parquet", index=False)
    val_df.to_parquet(out_dir / "val.parquet", index=False)

    print(f"prepare: {len(train_df)} train / {len(val_df)} val rows → {out_dir}/")


if __name__ == "__main__":
    main()
