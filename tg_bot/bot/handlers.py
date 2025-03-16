from aiogram import types


async def start(message: types.Message):
    await message.reply(
        "Здравствуйте! Загрузите Excel файл с данными столбцами: 'title', 'url', 'xpath'"
    )
