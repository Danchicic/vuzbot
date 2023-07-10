from aiogram.filters import CommandStart, Text, StateFilter
from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.redis import RedisStorage, Redis
from aiogram.fsm.context import FSMContext
from FSM.FSMdefault import FSMSnils

from lexicon import lexicon_ru
from keyboards import kb
import re

router: Router = Router()


@router.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    await state.set_state(FSMSnils.snils)
    await message.answer(text=lexicon_ru['start'])
    print(await state.get_state())


@router.message(StateFilter(FSMSnils.snils))
async def id_func(message: Message, state: FSMContext):
    if re.match(r"^\d{3}-\d{3}-\d{3}-\d{2}$", message.text):
        await state.update_data(snils=message.text)
        await message.answer(text=lexicon_ru['snils_correct'], reply_markup=kb.vuzkb())
        await state.clear()
    else:
        await message.answer(text=lexicon_ru['snils_uncorrect'])


