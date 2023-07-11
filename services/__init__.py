import json

import fake_useragent
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
from services.mirea import get_mirea_page


class GetVuzTable:
    def __init__(self, vuz_name, competition_name):
        self.competitionName = competition_name
        self.vuzName = vuz_name
        with open('/home/danya/PycharmProjects/vuz_bot/services/actions.json', 'r', encoding='utf-8') as f:
            self.actions = json.load(f)

    def mirea(self):
        from lexicon import competitions_mirea
        url = competitions_mirea[self.competitionName]
        print('class', url)
        return get_mirea_page(url=url)

    @staticmethod
    def get_comp() -> dict[str, str]:
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

        return dict(zip(competitions, hrefs))

    @staticmethod
    def mai():
        pass

    @staticmethod
    def mei():
        pass

    def get_main_table(self):
        # actions from json file
        for row in self.actions:
            if row['text'] == self.vuzName:
                return getattr(self, row['func'])()
