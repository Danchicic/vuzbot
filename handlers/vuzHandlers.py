from aiogram.filters import CommandStart, Text, StateFilter
from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.redis import RedisStorage, Redis
from aiogram.fsm.context import FSMContext

import lexicon
from FSM.FSMdefault import FSMSnils
from filters.filters import text_in_vuz
from lexicon import vuzes
from keyboards import kb
import re

router: Router = Router()
router.message.filter(text_in_vuz)


@router.message(Text(text=vuzes[0]))
async def first_vuz_check_comp(message: Message):
    await message.answer(text='Пожалуйста подождите некоторое время...')
    await message.answer(text='Выберите факультет для просмотра', reply_markup=kb.mirea_kb())


@router.message(Text(text=vuzes[1]))
async def id_func(message: Message):
    pass


@router.message(Text(text=vuzes[2]))
async def id_func(message: Message):
    pass
