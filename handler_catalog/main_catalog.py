from aiogram import Router, F
from help_files.main_wording import catalog_text
from help_files.keyboards import catalog_keyboard_main

from handler_catalog.tables import counting_records_icons
from photos.photo_add import catalog_list


from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery


rt = Router()

@rt.message(Command("catalog"))
async def catalog_open(message: Message):
    await message.answer(text=catalog_text, reply_markup=catalog_keyboard_main)
    
@rt.callback_query(F.data == "icons")
async def icons_variable(callback: CallbackQuery):
    list = catalog_list()
    k = 0
    count = counting_records_icons()
    if(len(count) != 0):
        for i in count:
            captions = f"Название: {i[2]} \n Описание: {i[3]} \n Цена: {i[7]}₽ \n Доступное количество для покупки: {i[6]}."
            await callback.bot.send_photo(chat_id=callback.message.chat.id, photo=list[k], caption=captions)
            k = k+1
    elif len(count) == 0:
        await callback.answer(f"Ничего нет. {count}")
    await callback.answer()