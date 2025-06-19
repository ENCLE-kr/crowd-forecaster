import os
import pandas as pd
from datetime import timedelta
from sklearn.preprocessing import StandardScaler

if __name__ == "__main__":
    scaler = StandardScaler()
    df_raw = pd.read_csv("./data/test/average_speed_test.txt", sep="\t")
    df_raw["date"] = pd.to_datetime(df_raw["date"])
    delta = df_raw["date"].iloc[1] - df_raw["date"].iloc[0]
    
    if delta >= timedelta(hours=1):
        pass