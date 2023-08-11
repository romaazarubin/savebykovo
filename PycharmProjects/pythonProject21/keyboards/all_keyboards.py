from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# first_markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
# first_markup.add(KeyboardButton("Да"), KeyboardButton("Возможно"))
#
# second_markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
# second_markup.add(KeyboardButton("ДА"), KeyboardButton("Естественно"))
#
# third_markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
# third_markup.add(KeyboardButton("Ок"), KeyboardButton("Понятно"))

first_markup_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Да', callback_data='yes')
        ],
        [
            InlineKeyboardButton(text='Возможно', callback_data='mb')
        ]
    ]
)

second_markup_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Да', callback_data='YES')
        ],
        [
            InlineKeyboardButton(text='Естественно', callback_data='naturally')
        ]
    ]
)

third_markup_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Ок', callback_data='ok')
        ],
        [
            InlineKeyboardButton(text='Понятно', callback_data='undst')
        ]
    ]
)

markup_inline = InlineKeyboardMarkup()
markup_inline.add(InlineKeyboardButton("Хочу внести 300Р", callback_data="data1"))
markup_inline.add(InlineKeyboardButton("Хочу внести 500Р", callback_data="data2"))
markup_inline.add(InlineKeyboardButton("Хочу внести 1000Р", callback_data="data3"))