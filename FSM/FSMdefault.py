from aiogram.filters.state import State, StatesGroup


class FSMUser(StatesGroup):
    snils = State()
    choose_vuz = State()
    choose_mark = State()
    choose_comp = State()


class FSMFavourite(StatesGroup):
    choose_favourite = State()
    change_vuz = State()
    choose_comps = State()
