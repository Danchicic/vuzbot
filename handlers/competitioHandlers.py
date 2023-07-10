from aiogram.filters import CommandStart, Text, StateFilter
from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.redis import RedisStorage, Redis
from aiogram.fsm.context import FSMContext
from FSM.FSMdefault import FSMSnils
from filters.filters import is_comp
from lexicon import vuzes
from keyboards import kb
import re

router: Router = Router()
router.message.filter(is_comp)
