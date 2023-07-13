import json

from services.mei import get_mei_students
from services.mirea import get_mirea_students


class GetVuzTable:
    def __init__(self, vuz_name, competition_name):
        self.competitionName = competition_name
        self.vuzName = vuz_name
        with open('/home/danya/PycharmProjects/vuz_bot/services/actions.json', 'r', encoding='utf-8') as f:
            self.actions = json.load(f)

    def mirea(self):
        from lexicon import competitions_mirea
        url = competitions_mirea.get(self.competitionName)
        if url is None:
            print('ВЫ чОу', competitions_mirea.competitions)
            raise 'Error services'
        # print(url)
        # print('class', url)
        return get_mirea_students(url=url)

    def mei(self):
        from lexicon import competitions_mei
        url = competitions_mei.get(self.competitionName)
        if url is None:
            print('ВЫ чОу', competitions_mei.competitions)
            raise 'Error services'
        return get_mei_students(url=url)

    @staticmethod
    def mai():
        pass

    @staticmethod
    def get_close_mark(my_mark: str, students) -> str:
        """
        :param my_mark:
        :param students:
        :return: MainStructure.snils
        """
        c = 0
        while 1:
            for snils, (priority, mark) in students.items():
                if int(mark) - int(my_mark) == c:
                    return snils
            else:
                c += 1

    def get_main_table(self):
        # actions from json file
        for row in self.actions:
            if row['text'] == self.vuzName:
                return getattr(self, row['func'])()


if __name__ == '__main__':
    table = GetVuzTable(competition_name='01.03.02\n(ИИИ)', vuz_name='МЭИ').mirea()
    print(table.students)
