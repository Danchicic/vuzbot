from aiogram.filters import CommandStart, StateFilter, Command
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from FSM.FSMdefault import FSMSnils
from lexicon import lexicon_ru
from keyboards import CompKeyboards
import re

router: Router = Router()


@router.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    await state.set_state(FSMSnils.snils)
    await message.answer(text=lexicon_ru['start'])


@router.message(StateFilter(FSMSnils.snils))
async def id_func(message: Message, state: FSMContext):
    if re.match(r"^\d{3}-\d{3}-\d{3}-\d{2}$", message.text):
        await state.update_data(snils=message.text)
        await message.answer(text=lexicon_ru['snils_correct'], reply_markup=CompKeyboards.vuzkb())
        await state.set_state(FSMSnils.choose_vuz)
    else:
        await message.answer(text=lexicon_ru['snils_uncorrect'])


"""
@router.message(Command(commands='favourite'))
@router.message(StateFilter(FSMSnils.choose_comp))
async def snils_command(message: Message, state: FSMContext):
    await state.set_state(FSMSnils.choose_mark)
    data = await state.get_data()
    kb = data['kb']
    await message.answer(text='Нажимайте на интересующие вас факультеты, когда закончите отправьте "stop"',
                         reply_markup=CompKeyboards(kb).get_kb())


@router.message(Command(commands='check'))
async def get_comp(message: Message):
    # from sql get hrefs and take position from
    # message.text replace from db вместо названия факультета
    # циклом про ним пройтись
    # students_list, sorted_students_list, budget = get_page(url=competitions[message.text])
    pass

"""


@router.message(Command(commands='snils'))
async def snils_command(message: Message, state: FSMContext):
    await state.set_state(FSMSnils.snils)
    await message.answer(text=lexicon_ru['change_snils'])


@router.message(Command(commands='vuz'))
async def vuz_command(message: Message, state: FSMContext):
    await state.set_state(FSMSnils.choose_vuz)
    await message.answer(text=lexicon_ru['change_vuz'], reply_markup=CompKeyboards.vuzkb())


@router.message(Command(commands='competition'))
async def comp_command(message: Message, state: FSMContext):
    await state.set_state(FSMSnils.choose_comp)
    data = await state.get_data()
    kb = data['kb']
    await message.answer(text=lexicon_ru['change_comp'], reply_markup=CompKeyboards(kb).get_kb())
