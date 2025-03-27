import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

while True:
    cursor.execute("SELECT store_id, title FROM stores")
    stores = cursor.fetchall()
    print(
        "\nвы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")

    for store in stores:
        print(f"{store[0]}. {store[1]}")

    store_id = input("\nвведите id магазина: ")
    if store_id == "0":
        print("выход из программы.")
        break
    store_id = int(store_id)

    cursor.execute("""
        SELECT products.title, categories.title, products.unit_price, products.stock_quantity
        FROM products
        JOIN categories ON products.category_code = categories.code
        WHERE products.store_id = ?
    """, (store_id,))

    products = cursor.fetchall()
    if not products:
        print("в данном магазине нет товаров или он не существует.")
        continue
    for product in products:
        print("\nназвание продукта:", product[0])
        print("категория:", product[1])
        print("цена:", product[2])
        print("количество на складе:", product[3])




conn.close()
