CATEGORY_MAP = {
    "food": "Food",
    "foods": "Food",
    "beverage": "Beverage",
    "beverages": "Beverage",
    "cleaning": "Cleaning",
    "clean": "Cleaning",
}

def normalize_categories(df):
    df = df.copy()
    df["category"] = (
        df["category"]
        .astype(str)
        .str.strip()
        .str.lower()
        .map(CATEGORY_MAP)
        .fillna(df["category"])
    )
    return df