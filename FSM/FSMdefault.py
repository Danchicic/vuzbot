from aiogram.filters.state import State, StatesGroup


class FSMSnils(StatesGroup):
    snils = State()
    choose_vuz = State()
    choose_comp = State()
    choose_mark = State()
