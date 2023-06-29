from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menukeyboard=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Inglizcha O'zbekcha"),
            KeyboardButton(text="O'zbekcha Inglizcha"),
        ],

    ],
    resize_keyboard=True
)


