from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon import vuzes, competitions_mirea, competitions_mei
import json


class CompKeyboards:
    def __init__(self, kb):
        self.kb: str = kb
        with open('/home/danya/PycharmProjects/vuz_bot/keyboards/actions.json', 'r', encoding='utf-8') as f:
            self.actions = json.load(f)

    @staticmethod
    def vuzkb() -> ReplyKeyboardMarkup:
        builder = ReplyKeyboardBuilder()
        buttons: list[KeyboardButton] = [KeyboardButton(text=vuz) for vuz in vuzes]
        builder.row(*buttons, width=4)
        return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

    @staticmethod
    def mirea_kb() -> ReplyKeyboardMarkup:
        builder = ReplyKeyboardBuilder()
        buttons: list[KeyboardButton] = [KeyboardButton(text=comp) for comp in competitions_mirea]
        builder.row(*buttons, width=4)
        return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

    @staticmethod
    def mei_kb() -> ReplyKeyboardMarkup:
        builder = ReplyKeyboardBuilder()
        buttons: list[KeyboardButton] = [KeyboardButton(text=comp) for comp in competitions_mei]
        builder.row(*buttons, width=1)
        return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

    def get_kb(self):
        # actions from json file
        for row in self.actions:
            if row['text'] == self.kb:
                return getattr(self, row['func'])()


if __name__ == '__main__':
    print(CompKeyboards('МИРЭА').get_kb())
