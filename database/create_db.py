import sqlite3


# Создание таблицы со словарем
def create_table():
    conn = sqlite3.connect('favourites.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE students
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, snils TEXT, chosen TEXT)''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_table()
