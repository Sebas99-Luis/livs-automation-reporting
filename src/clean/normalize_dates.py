import pandas as pd

def normalize_dates(df):
    df = df.copy()
    df["sale_date"] = pd.to_datetime(df["sale_date"], errors="coerce")
    return df