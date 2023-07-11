import asyncio
import logging
from aiogram.fsm.storage.redis import RedisStorage, Redis
from aiogram import Bot, Dispatcher
from config.config import Config, load_config
from handlers import user_handlers, vuzHandlers, competitioHandlers
from keyboards import kb

# Инициализируем логгер
logger = logging.getLogger(__name__)


# Функция конфигурирования и запуска бота
async def main():
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML',
                   )
    redis: Redis = Redis(host='localhost')
    storage: RedisStorage = RedisStorage(redis=redis)

    dp: Dispatcher = Dispatcher(storage=storage)
    dp.include_router(vuzHandlers.router)
    dp.include_router(user_handlers.router)
    dp.include_router(competitioHandlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
