import sqlite3

def connect_db():
    return sqlite3.connect('students.db')

def create_countries_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS countries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        );
    ''')
    conn.commit()
    conn.close()

def create_cities_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            area REAL DEFAULT 0,
            country_id INTEGER,
            FOREIGN KEY (country_id) REFERENCES countries(id)
        );
    ''')
    conn.commit()
    conn.close()

def create_students_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            city_id INTEGER,
            FOREIGN KEY (city_id) REFERENCES cities(id)
        );
    ''')
    conn.commit()
    conn.close()

def insert_countries():
    countries = [('Кыргызстан',), ('Германия',), ('Китай',)]
    conn = connect_db()
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO countries (title) VALUES (?)", countries)
    conn.commit()
    conn.close()

def insert_cities():
    cities = [
        ('Бишкек', 1500, 1),
        ('Ош', 1200, 1),
        ('Берлин', 891, 2),
        ('Мюнхен', 310, 2),
        ('Пекин', 1650, 3),
        ('Шанхай', 6340, 3),
        ('Гонконг', 1106, 3)
    ]
    conn = connect_db()
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)", cities)
    conn.commit()
    conn.close()

def insert_students():
    students = [
        ('Азиз', 'Шарипов', 1),
        ('Айгуль', 'Султанова', 1),
        ('Джон', 'Доу', 2),
        ('Мария', 'Кузнецова', 3),
        ('Максим', 'Лебедев', 4),
        ('Николай', 'Петров', 5),
        ('Иван', 'Петров', 6),
        ('Сергей', 'Иванов', 7),
        ('Светлана', 'Николаева', 1),
        ('Тимур', 'Рахимов', 2),
        ('Нурбек', 'Кыдыралиев', 3),
        ('Айжан', 'Токтобекова', 4),
        ('Жанна', 'Мамбетова', 5),
        ('Тимур', 'Жумабеков', 6),
        ('Дина', 'Абдуллаева', 7)
    ]
    conn = connect_db()
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)", students)
    conn.commit()
    conn.close()

def setup():
    create_countries_table()
    create_cities_table()
    create_students_table()
    insert_countries()
    insert_cities()
    insert_students()

if __name__ == '__main__':
    setup()
