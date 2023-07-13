import re

from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.types import Message

from aiogram.fsm.context import FSMContext
from FSM.FSMdefault import FSMUser
from keyboards import CompKeyboards
from lexicon import lexicon_ru

mark_router: Router = Router()
mark_router.message.filter(StateFilter(FSMUser.choose_mark))


@mark_router.message()
async def get_mark(message: Message, state: FSMContext):
    if re.match(r"\d{2,3}", message.text):
        print('Ввел оценку')
        await state.update_data(mark=message.text)
        data = await state.get_data()
        print(data)
        await message.answer(text=lexicon_ru['change_vuz'], reply_markup=CompKeyboards.vuzkb())
        await state.set_state(FSMUser.choose_vuz)
    else:
        await message.answer(text=lexicon_ru['uncorrect_data'])
