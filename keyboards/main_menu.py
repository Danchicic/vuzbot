from aiogram import Bot
from aiogram.types import BotCommand


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command='snils', description='Изменить снилс'),
        BotCommand(command='vuz', description='Изменить ВУЗ'),
        BotCommand(command='competition', description='Изменить факультет'),
        BotCommand(command='change_mark', description='Изменить свой балл'),
        BotCommand(command='favourite', description='**Посмотреть все свои факультеты'),

    ]
    await bot.set_my_commands(main_menu_commands)
