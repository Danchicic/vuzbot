from aiogram.filters import StateFilter
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from FSM.FSMdefault import FSMSnils
from keyboards import CompKeyboards
from lexicon import vuzes

router: Router = Router()
router.message.filter(StateFilter(FSMSnils.choose_vuz))


@router.message()
async def first_vuz_check_comp(message: Message, state: FSMContext):
    await state.set_state(FSMSnils.choose_comp)
    await state.update_data(kb=message.text)
    await message.answer(
        text='Выберите факультет для просмотра\n<b>Если хотите выбрать сразу несколько и добавить их в избранное введите команду /favourite </b>',
        reply_markup=CompKeyboards(message.text).get_kb())
