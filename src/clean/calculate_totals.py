import pandas as pd

def calculate_totals(df):
    df = df.copy()
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")

    df["total_amount"] = df["quantity"] * df["unit_price"]
    return df