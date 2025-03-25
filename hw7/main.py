from database import create_db
from models import add_products, list_products, update_quantity, update_price, delete_product, filter_products, search_products

if __name__ == "__main__":
    create_db()
    add_products()
    list_products()
    update_quantity(1, 20)
    update_price(2, 65.0)
    delete_product(3)
    print("Фильтрованные товары:")
    filter_products(100, 5)
    print("Поиск товаров:")
    search_products("мыло")