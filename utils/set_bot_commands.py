from aiogram import Bot
from aiogram import types

async def set_default_commands(bot: Bot):
    await bot.set_my_commands(
        [
            types.BotCommand(command="start", description="Botni ishga tushirish"),
            types.BotCommand(command="help", description="Yordam")
        ]
    )