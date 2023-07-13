import json
import sqlite3



# Вставка словаря в базу данных
def insert_student(snils: str, chosen):
    conn = sqlite3.connect('favourites.db')
    c = conn.cursor()

    # Сериализация словаря в строку
    chosen_str = json.dumps(chosen)

    # Вставка записи в базу данных
    c.execute("INSERT INTO students (snils, chosen) VALUES (?, ?)", (snils, chosen_str))

    conn.commit()
    conn.close()


# Получение словаря из базы данных по snils
def get_favourites(snils):
    conn = sqlite3.connect('favourites.db')
    c = conn.cursor()

    # Получение записи из базы данных
    c.execute("SELECT chosen FROM students WHERE snils=?", (snils,))
    result = c.fetchone()

    if result is not None:
        # Десериализация строки в словарь
        chosen_dict = json.loads(result[0])
        return chosen_dict
    else:
        return None


if __name__ == '__main__':
    # Пример использования
    # Создание таблицы (выполнять только один раз)

    # Вставка словаря в базу данных
    student_chosen = {'subject1': 'A', 'subject2': 'B', 'subject3': 'C'}
    insert_student('123456789', student_chosen)

    # Получение словаря из базы данных
    retrieved_chosen = get_favourites('123456789')
    print(retrieved_chosen)  # {'subject1': 'A', 'subject2': 'B', 'subject3': 'C'}
