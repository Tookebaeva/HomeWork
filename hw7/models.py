import sqlite3

def add_products():
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    products = [
        ("Мыло детское", 50.0, 10),
        ("Жидкое мыло с запахом ванили", 75.5, 5),
        ("Зубная паста", 120.0, 8),
        ("Шампунь", 250.0, 12),
        ("Гель для душа", 180.0, 7),
        ("Крем для рук", 90.0, 15),
        ("Лосьон для тела", 200.0, 4),
        ("Скраб для лица", 300.0, 6),
        ("Дезодорант", 150.0, 9),
        ("Пена для бритья", 175.0, 10),
        ("Шампунь против перхоти", 280.0, 3),
        ("Крем для лица", 350.0, 2),
        ("Зубная щетка", 100.0, 20),
        ("Гель для укладки волос", 140.0, 7),
        ("Одеколон", 400.0, 1)
    ]
    cursor.executemany("INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)", products)
    conn.commit()
    conn.close()

def update_quantity(product_id, new_quantity):
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, product_id))
    conn.commit()
    conn.close()

def update_price(product_id, new_price):
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
    conn.commit()
    conn.close()

def delete_product(product_id):
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()

def list_products():
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    for product in products:
        print(product)

def filter_products(price_limit, quantity_limit):
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE price < ? AND quantity > ?", (price_limit, quantity_limit))
    products = cursor.fetchall()
    conn.close()
    for product in products:
        print(product)

def search_products(keyword):
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE product_title LIKE ?", (f'%{keyword}%',))
    products = cursor.fetchall()
    conn.close()
    for product in products:
        print(product)