from aiogram import Router
from aiogram.filters import StateFilter, Command

from aiogram.types import Message, KeyboardButton
from aiogram.fsm.context import FSMContext
from FSM.FSMdefault import FSMFavourite
from lexicon import lexicon_ru
from keyboards import CompKeyboards

second_router: Router = Router()


@second_router.message(Command(commands='vuz'))
async def vuz_command(message: Message, state: FSMContext):
    await state.set_state(FSMFavourite.change_vuz)
    await message.answer(text=lexicon_ru['change_vuz_for_favourites'], reply_markup=CompKeyboards.vuzkb())


@second_router.message(StateFilter(FSMFavourite.change_vuz), Command(commands='stopA'))
async def save_comps(message: Message, state: FSMContext):
    data = await state.get_data()
    print('saved_comps', data)


@second_router.message(StateFilter(FSMFavourite.choose_comps), Command(commands='stopB'))
async def save_comps(message: Message, state: FSMContext):
    pass


@second_router.message()
async def get_names(message: Message, state: FSMContext):
    await state.update_data(vuz=message.text, reply_markup=[[KeyboardButton(text='stopA')]])  # kb -> stopA, stopB
