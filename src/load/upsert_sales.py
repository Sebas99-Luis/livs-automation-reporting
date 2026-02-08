def upsert_sales(df, conn):
    cursor = conn.cursor()

    sql = """
        INSERT INTO sales (
            sale_id, sale_date, product_name, category,
            quantity, unit_price, total_amount,
            payment_method, status
        )
        VALUES (
            %(sale_id)s, %(sale_date)s, %(product_name)s, %(category)s,
            %(quantity)s, %(unit_price)s, %(total_amount)s,
            %(payment_method)s, %(status)s
        )
        ON CONFLICT (sale_id)
        DO UPDATE SET
            sale_date = EXCLUDED.sale_date,
            product_name = EXCLUDED.product_name,
            category = EXCLUDED.category,
            quantity = EXCLUDED.quantity,
            unit_price = EXCLUDED.unit_price,
            total_amount = EXCLUDED.total_amount,
            payment_method = EXCLUDED.payment_method,
            status = EXCLUDED.status;
    """

    rows = df.to_dict(orient="records")

    for row in rows:
        cursor.execute(sql, row)

    conn.commit()
    cursor.close()