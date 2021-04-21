from loader import dp
from aiogram import types


@dp.message_handler(text="Контакты")
async def get_contacts(message: types.Message):
    await message.answer("ОмГТУ г-209")
