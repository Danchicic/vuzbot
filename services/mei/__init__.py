from typing import Type

import fake_useragent
import requests
from bs4 import BeautifulSoup

from type_hint import MainStructure, Competitions


def get_mei_comp() -> Type[Competitions]:
    url = 'https://pk.mpei.ru/inform/list.html'
    headers = {
        'User-Agent': fake_useragent.UserAgent().random,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    }
    page = requests.get(url=url, headers=headers)
    src = page.text
    # with open('index.html', 'w+') as f:
    #     f.write(src)
    with open('index.html') as f:
        src = f.read()

    src = BeautifulSoup(src, 'lxml')
    moscow_comp = src.find(class_='groupFilterMoscow').find_all('tr')
    comps = []
    hrefs = []

    for comp in moscow_comp:
        name, srcs = comp.find_all('td')
        comps.append(name.text)
        src = "https://pk.mpei.ru/" + srcs.find_all('a')[1].get('href')
        hrefs.append(src)
    Competitions.href = hrefs
    Competitions.name = comps

    return Competitions


def get_students() -> Type[MainStructure]:
    pass


def main():
    print(get_mei_comp())


if __name__ == '__main__':
    main()
