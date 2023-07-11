from aiogram.filters import CommandStart, Text, StateFilter
from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.redis import RedisStorage, Redis
from aiogram.fsm.context import FSMContext
from FSM.FSMdefault import FSMSnils
from filters.filters import is_comp
from lexicon import vuzes, competitions
from keyboards import kb
import re

from services.mirea import get_page

router: Router = Router()
router.message.filter(is_comp)


@router.message()
async def main(message: Message, state: FSMContext):
    students_list, sorted_students_list = get_page(url=competitions[message.text])
    print(students_list, sorted_students_list)
    data = await state.get_data()
    if data['snils'] in students_list:
        snils = data['snils']
        await message.answer(
            text=f"На данный момент вы на {list(sorted_students_list).index(snils) + 1} месте в соотношении с Первым приоритетом\n\nИ на {list(students_list).index(snils) + 1} месте без учета приоритета")
    else:
        await message.answer(
            text=f"Вы не найдены в списке")
