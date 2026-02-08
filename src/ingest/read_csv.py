import pandas as pd

REQUIRED_COLUMNS = [
    "sale_id",
    "sale_date",
    "product_name",
    "category",
    "quantity",
    "unit_price",
    "total_amount",
    "payment_method",
    "status"
]

def read_csv_file(path):
    df = pd.read_csv(path)

    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        return None, missing

    return df, None