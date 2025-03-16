import os
import sys
from aiogram import F, Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

from .services.db_service import init_db

from .handlers import (
    start,
    handle_document,
    handle_upload_request,
    parse_prices_handler,
    help_handler,
)


load_dotenv()


async def start_bot():
    API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    if not API_TOKEN:
        print("ERROR: Отсутствует переменная: TELEGRAM_BOT_TOKEN")
        sys.exit(-1)

    bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    init_db()

    dp.message.register(start, Command("start"))
    dp.message.register(handle_upload_request, F.text == "Загрузить файл")
    dp.message.register(handle_document, F.content_type == "document")
    dp.message.register(parse_prices_handler, F.text == "Рассчитать средние цены")
    dp.message.register(help_handler, F.text == "Помощь")
    dp.message.register(parse_prices_handler, Command("parse"))
    dp.message.register(help_handler, Command("help"))

    print("\n___Bot Started___")

    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio

    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        print("\n___Bot Finished___")
