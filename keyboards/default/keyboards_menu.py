from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Конференции"),
            KeyboardButton(text="Контакты")
        ],
        [
            KeyboardButton(text="Ближайшие события")
        ]
    ],
    resize_keyboard=True
)
