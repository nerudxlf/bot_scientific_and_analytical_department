from loader import dp, db
from aiogram import types


@dp.message_handler(text="Ближайшие события")
async def get_events(message: types.Message):
    conf_list = list(await db.get_nearest_conf())[0:5]
    out_str = ""
    for item in conf_list:
        out_str += f"Номер {item[0]}\nНазвание:\n{item[1]}\nОрганизаторы:\n{item[3]}\nСсылки:\n{item[2]}\nДата: {item[4]}:{item[5]}\n\n"
    await message.answer(out_str)
