from aiogram.filters import StateFilter
from aiogram import Router

from FSM.FSMdefault import FSMFavourite
from .favourite_fsm_handlers import second_router

# work only with FSMFavourite
favourite_router: Router = Router()
favourite_router.message.filter(StateFilter(FSMFavourite.choose_favourite))
favourite_router.include_router(second_router)
