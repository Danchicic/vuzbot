from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon import vuzes, competitions
from services.mirea import get_comp


def vuzkb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    buttons: list[KeyboardButton] = [KeyboardButton(text=vuz) for vuz in vuzes]
    builder.row(*buttons, width=4)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def mirea_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    buttons: list[KeyboardButton] = [KeyboardButton(text=comp) for comp in competitions]
    builder.row(*buttons, width=4)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
