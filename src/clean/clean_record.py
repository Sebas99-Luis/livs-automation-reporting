from .normalize_dates import normalize_dates
from .normalize_categories import normalize_categories
from .normalize_status import normalize_status
from .calculate_totals import calculate_totals

def clean_dataframe(df):
    df = normalize_dates(df)
    df = normalize_categories(df)
    df = normalize_status(df)
    df = calculate_totals(df)

    df = df.dropna(subset=["sale_id", "sale_date"])
    df = df.drop_duplicates(subset=["sale_id"])

    return df