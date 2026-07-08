import sqlite3

DB_NAME = "products.db"


def delete_product(title):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM products WHERE title = ?",
        (title,)
    )

    conn.commit()
    conn.close()


def update_product(old_title, price, category):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE products
        SET price = ?, category = ?
        WHERE title = ?
    """, (price, category, old_title))

    conn.commit()
    conn.close()
