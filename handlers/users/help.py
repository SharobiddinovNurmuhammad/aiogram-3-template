from loader import dp

from aiogram.types import Message
from aiogram.filters import Command


@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        text="Yordam"
    )