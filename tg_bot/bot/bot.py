import os
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

try:
    from .handlers import start  # Относительный импорт (для запуска через main.py)
except ImportError:
    from handlers import start  # Абсолютный импорт (для запуска напрямую)


load_dotenv()


async def start_bot():
    API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    if not API_TOKEN:
        print("ERROR: Отсутствует переменная: TELEGRAM_BOT_TOKEN")
        sys.exit(-1)

    bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.message.register(start, Command("start"))

    print("\n___Bot Started___")

    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio

    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        print("\n___Bot Finished___")
