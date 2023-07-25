import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import TOKEN as API_TOKEN
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

dp = Dispatcher()

async def main():
    await dp.start_polling(bot)

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Используй /help чтобы получить список доступных команд")
@dp.message(Command("help"))
async def send_help(message: types.Message):
    await message.reply("""
/help - это сообщение
/gen <твой текст> - сгенерировать картинку
/info - о боте
""")

@dp.message(Command("gen"))
async def echo(message: types.Message):
    arguments = message.get_args()
    await message.reply(arguments)
if __name__ == "__main__":
    asyncio.run(main())

