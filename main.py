import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import Message

from help_files.config import token
from help_files.main_wording import start_text

from handler_catalog import main_catalog

from handler_catalog.tables import create_table

# Включаем логирование
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=token)
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    create_table()
    await message.answer(start_text)
    
    

# Запуск процесса поллинга новых апдейтов
async def main():
    dp.include_router(main_catalog.rt)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())