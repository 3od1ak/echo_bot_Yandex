import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv


load_dotenv(".env.production")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv("YANDEX_BOT_TOKEN"))
dp = Dispatcher()


@dp.message()
async def cmd_start(message: types.Message):
    await message.answer(f'{message.text} {message.text}')


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
