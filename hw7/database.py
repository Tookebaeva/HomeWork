import sqlite3

def create_db():
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_title TEXT NOT NULL CHECK(length(product_title) <= 200),
            price REAL NOT NULL DEFAULT 0.0 CHECK(price >= 0),
            quantity INTEGER NOT NULL DEFAULT 0 CHECK(quantity >= 0)
        )
    ''')
    conn.commit()
    conn.close()