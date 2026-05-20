import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiohttp import web

TOKEN = os.getenv("8950640581:AAGZbbv2Ki98cmm-xJxRGdxdQTloYelNUss")
WEBHOOK_HOST = os.getenv("WEBHOOK_HOST")

WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("🎯 Quiz Bot ishlayapti!")

async def webhook_handler(request):
    data = await request.json()

    update = types.Update(**data)

    await dp.feed_update(bot, update)

    return web.Response()

async def on_startup(app):
    await bot.set_webhook(WEBHOOK_URL)

app = web.Application()

app.router.add_post(WEBHOOK_PATH, webhook_handler)

app.on_startup.append(on_startup)

web.run_app(
    app,
    host="0.0.0.0",
    port=int(os.getenv("PORT", 10000))
)
