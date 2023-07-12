import json
from typing import Type

from services.mirea import get_mirea_page
from type_hint import StructureForBot


class GetVuzTable:
    def __init__(self, vuz_name, competition_name):
        self.competitionName = competition_name
        self.vuzName = vuz_name
        with open('/home/danya/PycharmProjects/vuz_bot/services/actions.json', 'r', encoding='utf-8') as f:
            self.actions = json.load(f)

    def mirea(self) -> Type[StructureForBot]:
        from lexicon import competitions_mirea
        url = competitions_mirea.competitions[self.competitionName]
        # print('class', url)
        return get_mirea_page(url=url)

    @staticmethod
    def mai():
        pass

    @staticmethod
    def mei():
        pass

    def get_main_table(self) -> StructureForBot:
        # actions from json file
        for row in self.actions:
            if row['text'] == self.vuzName:
                return getattr(self, row['func'])()
