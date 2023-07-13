import re
from typing import Type

import fake_useragent
import requests
from bs4 import BeautifulSoup


def reformat_snils(original_snils: str):
    formatted_snils = '-'.join([original_snils[:3], original_snils[3:6], original_snils[6:9], original_snils[9:]])

    return formatted_snils


def get_mei_comp():
    """
    :return: Competitions, (more in type_hint)
    """
    url = 'https://pk.mpei.ru/inform/list.html'
    headers = {
        'User-Agent': fake_useragent.UserAgent().random,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    }

    # Отправка GET-запроса на указанный URL с заголовками
    page = requests.get(url=url, headers=headers)

    # Получение HTML-кода страницы
    src = page.text

    # Создание объекта BeautifulSoup для парсинга HTML
    src = BeautifulSoup(src, 'lxml')

    # Получение информации о соревнованиях в Москве
    moscow_comp = src.find(class_='groupFilterMoscow').find_all('tr')
    comps = []  # Список для хранения названий соревнований
    hrefs = []  # Список для хранения ссылок на соревнования

    for comp in moscow_comp:
        name, srcs = comp.find_all('td')
        comps.append(name.text)
        src = "https://pk.mpei.ru/" + srcs.find_all('a')[1].get('href')
        hrefs.append(src)

    return dict(zip(comps, hrefs))


def get_mei_students(url: str):
    """
    :param url:
    :return: StructureForBor, (more in type_hint)
    """
    # Устанавливаем необходимые заголовки для запроса
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": fake_useragent.UserAgent().random
    }

    # Отправляем GET-запрос по указанному URL с заданными заголовками
    page = requests.get(url=url, headers=headers)
    src = page.text

    # Создаем объект BeautifulSoup для парсинга HTML-кода страницы
    bs = BeautifulSoup(src, 'lxml')
    table = bs.find_all('tr')

    # Используем регулярное выражение для извлечения информации о количестве бюджетных мест
    budget = re.findall('Количество вакантных мест: \d{1,2}', bs.find('div', class_='title1').text)[0]

    students = {}
    for row in table[2:]:
        cells = row.findAll('td')

        # Пропускаем записи, если нет информации о приоритете или оценке студента
        if cells[-6].text == 'нет' or cells[1].text == '':
            continue

        snils = reformat_snils(cells[0].text.split()[-1])
        mark = cells[1].text
        priority = cells[-4].text

        students[snils] = (int(priority), mark)

    # Заполняем свойства объекта StructureForBot данными о студентах

    return students, dict(sorted(students.items(), key=lambda x: x[1][0])), budget


def main():
    print(get_mei_students(url='https://pk.mpei.ru//inform/list581bacc.html'))


if __name__ == '__main__':
    main()
