import asyncio
from telegram import Bot

# 🔐 توکن بات و آیدی عددی کانال
BOT_TOKEN = "7687238301:AAGXMxVR4EDlR284kM4SdDCoEtPZoIMVZb8"
CHANNEL_ID = -1002135689852 # اینو با آیدی عددی واقعی کانالت جایگزین کن

async def send_message():
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHANNEL_ID, text="✅ ربات Bloomberg فعال شد و آماده پخش اخبار است.")

if __name__ == '__main__':
    asyncio.run(send_message())
