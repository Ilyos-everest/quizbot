import os
import asyncio
from flask import Flask
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

app = Flask(name)

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("✅ Bot ishlayapti!")

@app.route("/")
def home():
    return "Bot is live!"

async def start_bot():
    await dp.start_polling(bot)

if name == "main":
    loop = asyncio.get_event_loop()
    loop.create_task(start_bot())

    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
