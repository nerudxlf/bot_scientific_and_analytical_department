from loader import dp
from aiogram import types


@dp.message_handler(text="Контакты")
async def get_contacts(message: types.Message):
    await message.answer("""Главный корпус ОмГТУ, кабинет: 209.\nНаучно-аналитический отдел ОмГТУ\nтелефон: +7 (3812) 65-35-36\nвнутренний: 4243\n\n""")
