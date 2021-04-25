from aiogram import types

from keyboards.default import menu
from loader import dp


@dp.message_handler(text="Информация")
async def show_menu(message: types.Message):
    await message.answer("Выберите пункт ниже", reply_markup=menu)
