from aiogram import Router
from aiogram.filters import StateFilter

from aiogram.types import Message

from aiogram.fsm.context import FSMContext
from FSM.FSMdefault import FSMUser
from services import GetVuzTable

compets_router: Router = Router()
compets_router.message.filter(StateFilter(FSMUser.choose_comp))

"""
@router.message(StateFilter(FSMSnils.choose_mark))
async def add_comp(message: Message, state: FSMContext):
    # add sql
    pass


@router.message(StateFilter(FSMSnils.choose_mark))
@router.message(Text(text='stop'))
async def stop_favourite(message: Message, state: FSMContext):
    await message.answer(text=lexicon_ru['stop'])
"""


@compets_router.message()
async def send_statistic(message: Message, state: FSMContext):
    data = await state.get_data()
    print('data', data)
    students, sorted_students, budget = GetVuzTable(data['kb'], message.text).get_main_table()

    if data['snils'] in students:
        snils = data['snils']
        await message.answer(
            text=f"{list(sorted_students).index(snils) + 1} место в соотношении с Первым приоритетом\n\n{list(students).index(snils) + 1} место без учета приоритета\n<b><u>{budget}</u></b>")
    else:
        my_mark = data['mark']
        my_mythic_snils = GetVuzTable.get_close_mark(my_mark, students)
        print(my_mythic_snils)
        await message.answer(
            text=f"Вы не найдены в списке подавших оригинал,\nНо при подаче оригинала вы будете на {list(students).index(my_mythic_snils) + 1} месте, <b>Без учета приоритета</b>\nИ на {list(sorted_students).index(my_mythic_snils) + 1} месте с учетом приоритета")
