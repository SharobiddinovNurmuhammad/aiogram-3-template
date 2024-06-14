from loader import dp

from aiogram.types import Message

@dp.message()
async def echo(message: Message):
    await message.reply(
        text=message.text
    )