import os
from aiogram import types

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from .services.excel_service import read_excel

UPLOAD_DIR = "data/"


async def start(message: types.Message):
    reply_keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Загрузить файл")]],
        resize_keyboard=True,
    )
    await message.reply("Привет! Выберите действие:", reply_markup=reply_keyboard)

    # await message.reply(
    #     "Здравствуйте! Загрузите Excel файл с данными столбцами: 'title', 'url', 'xpath'"
    # )


async def handle_upload_request(message: types.Message):
    if message.text == "Загрузить файл":
        await message.reply("Пожалуйста, отправьте файл в формате .xlsx.")


async def handle_document(message: types.Message):
    document = message.document
    if not document.file_name.endswith(".xlsx"):
        await message.reply("Пожалуйста, загрузите файл в формате .xlsx.")
        return

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
    except ValueError as e:
        await message.reply(str(e))
