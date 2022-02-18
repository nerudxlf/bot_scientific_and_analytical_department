from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import db, dp
from states import ConfState


@dp.message_handler(text="Конференции")
async def get_conf(message: types.Message):
    answer = await db.get_id_and_name_conf()
    out_string = ""
    for item in list(answer):
        out_string += f"{item[0]}.\n{item[1]}\n"
    out_string += "\n\nВведите номер конференции, чтобы узнать подробную информацию или 0 чтобы закончить"
    await message.answer(out_string)
    await ConfState.Q1.set()


@dp.message_handler(state=ConfState.Q1)
async def get_need_conf(message: types.Message, state: FSMContext):
    try:
        answer = int(message.text)
    except ValueError:
        await message.answer("Введите номер конференции или 0 чтобы закончить")
        return
    if str(message.text) == "0":
        await state.finish()
        return
    data_list = list(await db.get_full_info(co_id=answer))
    name = data_list[1]
    organizer = data_list[3]
    links = data_list[2]
    date_start = data_list[4]
    data_end = data_list[5]
    out_string = f"Название конференции:\n{name}\n" \
                 f"Организаторы:\n{organizer}\n" \
                 f"Ссылки:\n{links}\n" \
                 f"Дата:\n{date_start} - {data_end}"
    await message.answer(out_string)
    await state.finish()
