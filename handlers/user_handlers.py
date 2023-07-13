from aiogram import Router
from aiogram.filters import CommandStart, StateFilter, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from FSM.FSMdefault import FSMUser, FSMFavourite
from lexicon import lexicon_ru
from keyboards import CompKeyboards
import re

default_router: Router = Router()


@default_router.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(FSMUser.snils)
    await message.answer(text=lexicon_ru['start'])


@default_router.message(StateFilter(FSMUser.snils))
async def id_func(message: Message, state: FSMContext):
    if re.match(r"^\d{3}-\d{3}-\d{3}-\d{2}$", message.text):
        await state.update_data(snils=message.text)
        await message.answer(text=lexicon_ru['snils_correct'])
        await state.set_state(FSMUser.choose_mark)
    else:
        await message.answer(text=lexicon_ru['snils_uncorrect'])


@default_router.message(Command(commands='snils'))
async def snils_command(message: Message, state: FSMContext):
    await state.set_state(FSMUser.snils)
    await message.answer(text=lexicon_ru['change_snils'])


@default_router.message(Command(commands='vuz'))
async def vuz_command(message: Message, state: FSMContext):
    await state.set_state(FSMUser.choose_vuz)
    await message.answer(text=lexicon_ru['change_vuz'], reply_markup=CompKeyboards.vuzkb())


@default_router.message(Command(commands='competition'))
async def comp_command(message: Message, state: FSMContext):
    await state.set_state(FSMUser.choose_comp)
    data = await state.get_data()
    kb = data['kb']
    await message.answer(text=lexicon_ru['change_comp'], reply_markup=CompKeyboards(kb).get_kb())


@default_router.message(Command(commands='change_mark'))
async def mark_command(message: Message, state: FSMContext):
    await state.set_state(FSMUser.choose_mark)
    await state.update_data(mark=message.text)
    await message.answer(text=lexicon_ru['change_mark'])


# Переход в состояние второго порядка
@default_router.message(StateFilter(FSMUser.choose_comp), Command(commands='favourite'))
async def favourite_command(message: Message, state: FSMContext):
    await state.set_state(FSMFavourite.choose_favourite)
    data = await state.get_data()
    kb = data['kb']
    print('Я тут???')
    await message.answer(text='Нажимайте на интересующие вас факультеты, когда закончите отправьте "stop"',
                         reply_markup=CompKeyboards(kb).get_kb())
