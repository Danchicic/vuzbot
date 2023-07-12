from aiogram.filters import StateFilter
from aiogram import Router
from aiogram.types import Message

from aiogram.fsm.context import FSMContext
from FSM.FSMdefault import FSMSnils
from services import GetVuzTable

router: Router = Router()
router.message.filter(StateFilter(FSMSnils.choose_comp))

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


@router.message()
async def mirea(message: Message, state: FSMContext):
    # students_list, sorted_students_list, budget = get_page(url=competitions_mirea[message.text])
    data = await state.get_data()
    print('data', data)
    table = GetVuzTable(data['kb'], message.text).get_main_table()

    if data['snils'] in table.students:
        snils = data['snils']
        await message.answer(
            text=f"{list(table.sorted_students).index(snils) + 1} место в соотношении с Первым приоритетом\n\n{list(table.students).index(snils) + 1} место без учета приоритета\n<b><u>{table.budget}</u></b>")
    else:
        await message.answer(
            text=f"Вы не найдены в списке")
