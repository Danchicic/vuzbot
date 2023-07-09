from aiogram.filters import Command, CommandStart, Text
from aiogram import Router
from aiogram.types import Message, CallbackQuery

import keyboards as keyb

router: Router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text='qq')

