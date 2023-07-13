import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import fake_useragent
import re
from selenium.webdriver.common.by import By


def get_mirea_students(url: str, original: int = 1):
    """
    Функция для получения информации о студентах МИРЭА.

    Аргументы:
    - url (str): URL-адрес страницы с информацией о студентах.
    - original (int): Флаг для отбора только оригинальных мест поступления (по умолчанию 1).
    """
    headers: dict = {
        "user-agent": fake_useragent.UserAgent().random,
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    }
    # Отправляем GET-запрос на указанный URL с заданными заголовками и параметрами
    page = requests.get(url=url, headers=headers, params={'accepted': original}).text
    page = BeautifulSoup(page, 'lxml')
    # Получаем бюджетную квоту из второго абзаца страницы
    budget = page.find_all('p')[1].text
    # Получаем все строки таблицы с информацией о студентах
    table = page.find_all('tr')
    students = {}
    # Проходимся по каждой строке таблицы, начиная со второй строки
    for student in table[1:]:
        # Получаем оригинальный идентификатор студента
        original_id = student.find(class_='fio').text.strip()
        # Получаем приоритет поступления студента
        priority = student.find(class_='accepted').text.strip()
        # Получаем последнюю суммарную оценку студента
        mark = student.find_all(class_='sum')[-1].text.strip()
        # Добавляем информацию о студенте в словарь students
        students[original_id] = int(priority), mark

    return students, dict(sorted(students.items(), key=lambda x: x[1][0])), budget


def get_mirea_comp():
    # Определение URL-адреса сайта
    url = 'https://priem.mirea.ru/accepted-entrants-list/'

    # Генерация случайного user agent
    user = fake_useragent.UserAgent().random

    # Настройка параметров Chrome-браузера
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={user}")  # Установка user agent для Chrome-браузера
    options.add_argument("--headless")  # Запуск Chrome в безголовом режиме (без открытия окна)

    # Создание экземпляра драйвера Chrome
    driver = webdriver.Chrome(options=options)

    # Список для хранения информации о соревнованиях
    competitions = []

    # Список для хранения ссылок на страницы с подробной информацией о соревнованиях
    hrefs = []

    try:
        # Открытие URL-адреса сайта в браузере
        driver.get(url=url)

        # Поиск всех элементов с информацией о соревнованиях
        competitions_web = driver.find_elements(By.CLASS_NAME, 'npsTitle')

        # Поиск всех элементов источников
        srcs = driver.find_elements(By.CLASS_NAME, 'rowCommon')

        # Получение ссылок на страницы с подробной информацией о соревнованиях
        for src in srcs:
            hrefs.append(src.find_element(By.CLASS_NAME, 'showListingBtn').get_property('href'))

        # Обход каждого элемента с информацией о соревновании
        for comp in competitions_web:
            # comp = comp.find_element(By.CLASS_NAME, 'compType')

            # Поиск всех элементов <td> внутри элемента с информацией о соревновании
            compets = comp.find_elements(By.TAG_NAME, 'td')

            # Добавление информации о соревновании в список competitions
            for com in compets:
                if com.text.strip().split() != [] and re.match(r"\d{2}.\d{2}.\d{2}", com.text.strip().split()[0]):
                    competitions.append(f"{comp.text.split()[0]}\n{com.text.split()[-1]}")
                    continue
                if com.text == 'только платные места':
                    competitions.pop(-1)

    except Exception as ex:
        print(ex)

    finally:
        # Закрытие окна браузера
        driver.close()

        # Завершение работы драйвера (закрытие всех ассоциированных окон и процесса WebDriver)
        driver.quit()

    # Создание словаря, сопоставляющего соревнования и соответствующие им ссылки

    # Возврат класса Competitions
    return dict(zip(competitions, hrefs))


def main() -> None:
    # print(get_mirea_page(
    #     'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1748205428624334134').students)
    print(get_mirea_comp())


if __name__ == '__main__':
    main()
