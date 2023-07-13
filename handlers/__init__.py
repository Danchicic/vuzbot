from aiogram import Router

from .competitioHandlers import compets_router
from .markHandler import mark_router
from .user_handlers import default_router
from .vuzHandlers import vuz_router

main_router: Router = Router()
main_router.include_router(default_router)
main_router.include_router(vuz_router)

main_router.include_router(mark_router)
main_router.include_router(compets_router)
