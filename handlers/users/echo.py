from aiogram import types

from keyboards.default import menu
from loader import dp


@dp.message_handler()
async def bot_echo(message: types.Message):
    await message.answer(message.text, reply_markup=menu)
