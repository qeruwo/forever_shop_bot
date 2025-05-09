from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

catalog_keyboard_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Значки", callback_data='icons'), InlineKeyboardButton(text="Брелки", callback_data='trinket'), InlineKeyboardButton(text="Булавки", callback_data='pins')],
    [InlineKeyboardButton(text="Вернуться назад", callback_data='back_menu')],
])