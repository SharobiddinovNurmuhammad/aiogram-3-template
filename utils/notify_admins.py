import logging

from aiogram import Bot
from data.config import ADMINS

async def on_startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(admin, "Bot ishga tushdi")
        except Exception as err:
            logging.exception(err)

async def on_shutdown_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(int(admin), "Bot ishdan to'xtadi")
        except Exception as err:
            logging.exception(err) # Xatolik haqida logging