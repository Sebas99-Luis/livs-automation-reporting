STATUS_MAP = {
    "completed": "completed",
    "complete": "completed",
    "done": "completed",
    "refunded": "refunded",
    "refund": "refunded",
    "cancelled": "cancelled",
    "canceled": "cancelled",
}

def normalize_status(df):
    df = df.copy()
    df["status"] = (
        df["status"]
        .astype(str)
        .str.strip()
        .str.lower()
        .map(STATUS_MAP)
        .fillna("unknown")
    )
    return df