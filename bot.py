from aiogram import Bot, Dispatcher
import asyncio
import logging
from handlers import router as handlers_router
import os

from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")

if not BOT_TOKEN:
    logging.error("Переменная окружения BOT_TOKEN не найдена!")
    exit()

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Регистрируем роутер с обработчиками
    dp.include_router(handlers_router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
