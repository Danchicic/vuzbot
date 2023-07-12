from typing import Type

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import fake_useragent
import re
from selenium.webdriver.common.by import By
from type_hint import Competitions, StructureForBot


def get_mirea_page(url: str) -> Type[StructureForBot]:
    headers: dict = {
        "user-agent": fake_useragent.UserAgent().random,
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    }
    """"""
    page = requests.get(url=url, headers=headers, params={'accepted': 1}).text
    with open('index.html', 'w+') as f:
        f.write(page)

    #
    # with open('index.html') as f:
    #     src = f.read()
    #     page = src
    page = BeautifulSoup(page, 'lxml')
    budget = page.find_all('p')[1].text

    table = page.find_all('tr')
    students = {}
    for student in table[1:]:
        original_id = student.find(class_='fio').text.strip()
        priority = student.find(class_='accepted').text.strip()
        mark = student.find_all(class_='sum')[-1].text.strip()

        students[original_id] = int(priority), mark
    StructureForBot.students = students
    StructureForBot.sorted_students = dict(sorted(students.items(), key=lambda x: x[1][0]))
    StructureForBot.budget = budget
    return StructureForBot


def get_mirea_comp() -> Type[Competitions]:
    url = 'https://priem.mirea.ru/accepted-entrants-list/'
    user = fake_useragent.UserAgent().random
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={user}")
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    competitions = []
    hrefs = []
    try:
        driver.get(url=url)
        competitions_web = driver.find_elements(By.CLASS_NAME, 'npsTitle')
        srcs = driver.find_elements(By.CLASS_NAME, 'rowCommon')
        for src in srcs:
            hrefs.append(src.find_element(By.CLASS_NAME, 'showListingBtn').get_property('href'))
        for comp in competitions_web:
            # comp = comp.find_element(By.CLASS_NAME, 'compType')

            compets = comp.find_elements(By.TAG_NAME, 'td')
            for com in compets:
                if com.text.strip().split() != [] and re.match(r"\d{2}\.\d{2}\.\d{2}", com.text.strip().split()[0]):
                    competitions.append(f"{comp.text.split()[0]}\n{com.text.split()[-1]}")
                    continue
                if com.text == 'только платные места':
                    competitions.pop(-1)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

    Competitions.competitions = dict(zip(competitions, hrefs))
    return Competitions


def main() -> None:
    # print(get_mirea_page(
    #     'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1748205428624334134').students)
    print(get_mirea_comp().competitions)


if __name__ == '__main__':
    main()
