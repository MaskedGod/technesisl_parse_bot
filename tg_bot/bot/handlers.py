import os
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from .services.parser_services import parse_prices
from .services.db_service import save_to_db
from .services.excel_service import read_excel

UPLOAD_DIR = "data/"


async def start(message: types.Message):
    # Создаем клавиатуру с кнопками
    reply_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Загрузить файл")],
            [KeyboardButton(text="Рассчитать средние цены")],
            [KeyboardButton(text="Помощь")],
        ],
        resize_keyboard=True,
    )
    await message.reply(
        "Здравствуйте! Выберите действие:\n"
        "- Загрузить файл: отправьте Excel-файл с данными.\n"
        "- Рассчитать средние цены: выполните парсинг сайтов из базы данных.\n"
        "- Помощь: получите информацию о командах.",
        reply_markup=reply_keyboard,
    )


async def handle_upload_request(message: types.Message):
    if message.text == "Загрузить файл":
        await message.reply("Пожалуйста, отправьте файл в формате .xlsx.")


async def handle_document(message: types.Message):
    document = message.document

    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    file_path = os.path.join(UPLOAD_DIR, document.file_name)
    await message.bot.download(document, destination=file_path)

    try:
        df = read_excel(file_path)
        formatted_data = "\n".join(
            [
                f"Название: {row['title']}, Ссылка: {row['url']}, XPath: {row['xpath']}"
                for _, row in df.iterrows()
            ]
        )
        await message.reply(f"Файл успешно прочитан:\n{formatted_data}")

        save_to_db(df)
        await message.reply("Данные успешно сохранены в базу данных.")
    except ValueError as e:
        await message.reply(str(e))


async def parse_prices_handler(message: types.Message):
    if message.text == "Рассчитать средние цены" or message.text.startswith("/parse"):
        try:
            result = parse_prices()
            await message.reply(result)
        except Exception as e:
            await message.reply(f"Ошибка при парсинге: {e}")


async def help_handler(message: types.Message):
    if message.text == "Помощь" or message.text.startswith("/help"):
        await message.reply(
            "Доступные команды:\n"
            "- /start: начать работу с ботом.\n"
            "- Загрузить файл: отправьте Excel-файл с данными (столбцы: title, url, xpath).\n"
            "- Рассчитать средние цены: выполните парсинг сайтов из базы данных.\n"
            "- Помощь: получите информацию о командах."
        )
