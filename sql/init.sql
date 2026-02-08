CREATE TABLE IF NOT EXISTS sales (
    sale_id TEXT PRIMARY KEY,
    sale_date TIMESTAMP,
    product_name TEXT,
    category TEXT,
    quantity INTEGER,
    unit_price NUMERIC(10,2),
    total_amount NUMERIC(10,2),
    payment_method TEXT,
    status TEXT
);