from loader import dp

from aiogram.types import Message
from aiogram.filters import CommandStart

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        text='Salom, {}'.format(message.from_user.full_name)
    )
