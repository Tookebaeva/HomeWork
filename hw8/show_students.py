import sqlite3

def connect_db():
    return sqlite3.connect('students.db')

def show_students(city_id):
    conn = connect_db()
    cursor = conn.cursor()
    query = '''
    SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
    FROM students
    JOIN cities ON students.city_id = cities.id
    JOIN countries ON cities.country_id = countries.id
    WHERE cities.id = ?
    '''
    cursor.execute(query, (city_id,))
    students = cursor.fetchall()
    conn.close()

    if students:
        for student in students:
            print(
                f'имя: {student[0]}, фамилия: {student[1]}, страна: {student[2]}, город: {student[3]}, площадь города: {student[4]}')
    else:
        print("нет учеников в выбранном городе.")


def main():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()
    conn.close()

    print(
        "вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
    for city in cities:
        print(f'{city[0]}. {city[1]}')

    while True:
        try:
            city_id = int(input("введите id города: "))
            if city_id == 0:
                print("выход из программы.")
                break
            show_students(city_id)
        except ValueError:
            print("введите корректное id.")


if __name__ == "__main__":
    main()
