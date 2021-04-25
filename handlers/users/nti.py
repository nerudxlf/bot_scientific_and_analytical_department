from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default import menu_nti, menu
from loader import db, dp
from states import NtiState


@dp.message_handler(text="По НТИ")
async def get_nti_menu(message: types.Message):
    await message.answer("Выберите пункт ниже", reply_markup=menu_nti)
    await NtiState.Q1.set()


@dp.message_handler(state=NtiState.Q1)
async def get_info_nti(message: types.Message, state: FSMContext):
    if str(message.text).lower() == "в начало":
        await message.answer("Выберите пункт ниже", reply_markup=menu)
        await state.finish()
        return
    if str(message.text).lower() == "справка по нти":
        await message.answer("Какой то ответ")
        return
    data_list = await db.get_info_nti(str(message.text).lower())
    if not data_list:
        await message.answer("Данные отсутствуют")
        return
    else:
        out_string = ""
        for item in list(data_list):
            out_string += f"{item[0]}.\n{item[1]}\n"
        await message.answer(out_string)