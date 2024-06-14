import asyncio
import logging

from loader import dp, bot
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify, on_shutdown_notify
from utils.set_bot_commands import set_default_commands

async def on_startup(dispatcher):
    # Bot kommandalarini ishga tushirish
    await set_default_commands(bot)

    # Bot ishga tushgani haqida adminlarga xabar berish
    dispatcher.startup.register(on_startup_notify)

    # Bot ishdan to'xtagani haqida adminlarga xabar berish
    dispatcher.shutdown.register(on_shutdown_notify)


async def main():
    # on_startup funksiyasini ishga tushirish
    await on_startup(dp)

    #Botni ishga tushirish
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")