from aiogram.filters import StateFilter, Text
from aiogram import Router
from aiogram.types import Message

from aiogram.fsm.context import FSMContext
from FSM.FSMdefault import FSMSnils

from lexicon import competitions, lexicon_ru

from services.mirea import get_page

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
async def main(message: Message, state: FSMContext):
    students_list, sorted_students_list, budget = get_page(url=competitions[message.text])
    data = await state.get_data()
    # await state.set_state(FSMSnils.choose_comp)
    if data['snils'] in students_list:
        snils = data['snils']
        # a = await state.get_data()
        await message.answer(
            text=f"{list(sorted_students_list).index(snils) + 1} место в соотношении с Первым приоритетом\n\n{list(students_list).index(snils) + 1} место без учета приоритета\n<b><u>{budget}</u></b>")
    else:
        await message.answer(
            text=f"Вы не найдены в списке")
