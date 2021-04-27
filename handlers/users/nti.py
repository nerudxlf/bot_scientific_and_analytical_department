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
        await message.answer("""
Сообщество Национальной технологической инициативы (НТИ 20.35) объединяет предпринимателей, 
инвесторов, экспертов, представителей науки и образования. По итогам стратегической сессии 
«Форсайт-флот», состоявшейся в мае 2015 года определены девять перспективных рынков 
(https://nti2035.ru/markets/): Аэронет, Автонет, Маринет, Нейронет, Хелснет, Фуднет, 
Энерджинет, Технет, Сэйфнет. Совместно с точкой кипения ОмГТУ научно-аналитическим отделом 
определено соответствие конференциям ОмГТУ рынкам НТИ. К сожалению, многие конференции 
оказались вне повестки НТИ.""")
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
