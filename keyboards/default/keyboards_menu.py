from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Конференции"),
            KeyboardButton(text="По НТИ"),
            KeyboardButton(text="По СНТР")
        ],
        [
            KeyboardButton(text="Ближайшие события"),
            KeyboardButton(text="Контакты")
        ]
    ],
    resize_keyboard=True
)

menu_nti = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="АэроНет"),
            KeyboardButton(text="НейроНет"),
            KeyboardButton(text="ТехНет"),
            KeyboardButton(text="EduNet"),
        ],
        [
            KeyboardButton(text="ФудНет"),
            KeyboardButton(text="СейфНет"),
            KeyboardButton(text="WearNet"),
            KeyboardButton(text="СпортНет"),
        ],
        [
            KeyboardButton(text="Прочие"),
            KeyboardButton(text="Справка по НТИ"),
            KeyboardButton(text="В начало")
        ]
    ],
    resize_keyboard=True
)

menu_sntr = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="P1"),
            KeyboardButton(text="P2"),
            KeyboardButton(text="P3")
        ],
        [
            KeyboardButton(text="P4"),
            KeyboardButton(text="P5"),
            KeyboardButton(text="P6")
        ],
        [
            KeyboardButton(text="P7"),
            KeyboardButton(text="Справка по СНТР"),
            KeyboardButton(text="В начало")
        ]
    ],
    resize_keyboard=True
)
