from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default import menu_sntr, menu
from loader import db, dp
from states import SntrState


@dp.message_handler(text="По СНТР")
async def get_sntr_menu(message: types.Message):
    await message.answer("Выберите пункт ниже", reply_markup=menu_sntr)
    await SntrState.Q1.set()


@dp.message_handler(state=SntrState.Q1)
async def get_info_sntr(message: types.Message, state: FSMContext):
    if str(message.text).lower() == "в начало":
        await message.answer("Выберите пункт ниже", reply_markup=menu)
        await state.finish()
        return
    if str(message.text).lower() == "справка по снтр":
        await message.answer("""Стратегии научно-технологического развития РФ определены указом Президента в редакции Указа Президента Российской Федерации от 15.03.2021 № 143.  Участие организаций в участии в этом развитии определяется. Соответсвие публикаций СНТР определяется в том числе соответствии с приказом Минобрнауки России от 16.04.2019 N 234 "Об утверждении методик расчета целевых и дополнительных показателей для мониторинга  национального проекта "Наука" и федеральных проектов.

Приоритетные направления научно-технологического развития РФ являются

P1. Цифровые технологии, искусственный интеллект, новые материалы;

P2. Экологически чистая и ресурсосберегающая энергетика, новые источники энергии; 

P3. Персонализированная медицина и высокотехнологичное здравоохранение;

P4. Рациональное агро- и аквахозяйство, защита экологии, безопасные продукты питания; 

P5. Противодействие угрозам национальной и индивидуальной безопасности; 

P6. Связность территории Российской федерации; 

P7. Эффективное взаимодействие человека, природы и технологий""")
        return
    data_list = await db.get_info_sntr(str(message.text).lower())
    if not data_list:
        await message.answer("Данные отсутствуют")
        return
    else:
        out_string = ""
        for item in list(data_list):
            out_string += f"{item[0]}.\n{item[1]}\n"
        await message.answer(out_string)
