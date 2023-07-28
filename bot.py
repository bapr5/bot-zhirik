import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import TOKEN as API_TOKEN
import text2image
from os import remove
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

dp = Dispatcher()

def extract_args(message):
    return " ".join(message.text.split(maxsplit=1)[1:])

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
async def args(message: types.Message):
    arguments = extract_args(message)
    text2image.gen_image(txt=arguments)
    image=types.FSInputFile("buffer.png")
    await message.answer_photo(
    image,
    caption="жирик"
)
    remove("buffer.png")
    

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

