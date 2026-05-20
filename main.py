import os
from flask import Flask, request
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

TOKEN = os.getenv("8950640581:AAGZbbv2Ki98cmm-xJxRGdxdQTloYelNUss")

bot = Bot(token=TOKEN)
dp = Dispatcher()

app = Flask(name)

WEBHOOK_PATH = f"/{TOKEN}"
WEBHOOK_URL = f"{os.getenv('RENDER_EXTERNAL_URL')}{WEBHOOK_PATH}"


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("✅ Professional Quiz Bot ishlayapti!")


@app.route("/")
def home():
    return "Bot is running"


@app.route(WEBHOOK_PATH, methods=["POST"])
def webhook():
    update = types.Update.model_validate(request.json)

    asyncio.run(dp.feed_update(bot, update))

    return "ok"


async def set_webhook():
    await bot.set_webhook(WEBHOOK_URL)
    print("Webhook:", WEBHOOK_URL)


if name == "main":
    asyncio.run(set_webhook())

    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
