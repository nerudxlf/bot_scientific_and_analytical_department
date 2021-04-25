from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.default import menu
from loader import dp


@dp.message_handler(Command("menu"))
async def bot_start(message: types.Message):
    await message.answer("Выберите пункт ниже", reply_markup=menu)
