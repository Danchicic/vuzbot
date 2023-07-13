from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from FSM.FSMdefault import FSMUser
from keyboards import CompKeyboards
from lexicon import lexicon_ru

vuz_router: Router = Router()
vuz_router.message.filter(StateFilter(FSMUser.choose_vuz))


@vuz_router.message()
async def first_vuz_check_comp(message: Message, state: FSMContext):
    await state.set_state(FSMUser.choose_comp)
    await state.update_data(kb=message.text)
    data = await state.get_data()
    print('send wrong', data)
    await message.answer(
        text=lexicon_ru['change_comp'],
        reply_markup=CompKeyboards(message.text).get_kb())
