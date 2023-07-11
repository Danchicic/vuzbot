from aiogram.filters import Text, StateFilter
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from FSM.FSMdefault import FSMSnils
from keyboards import CompKeyboards
from lexicon import vuzes

router: Router = Router()
router.message.filter(StateFilter(FSMSnils.choose_vuz))


@router.message(Text(text=vuzes[0]))
async def first_vuz_check_comp(message: Message, state: FSMContext):
    await state.set_state(FSMSnils.choose_comp)
    await state.update_data(kb='МИРЭА')
    await message.answer(
        text='Выберите факультет для просмотра\n<b>Если хотите выбрать сразу несколько и добавить их в избранное введите команду /favourite </b>',
        reply_markup=CompKeyboards('МИРЭА').get_kb())


@router.message(Text(text=vuzes[1]))
async def id_func(message: Message):
    pass


@router.message(Text(text=vuzes[2]))
async def id_func(message: Message):
    pass
