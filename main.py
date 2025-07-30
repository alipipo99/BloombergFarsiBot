import feedparser
import logging
import sys
import asyncio
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# تنظیمات ربات
BOT_TOKEN = "7687238301:AAGXMxVR4EDlR284kM4SdDCoEtPZoIMVZb8"
CHANNEL_ID = "-1002006111361"
BLOOMBERG_FEED = "https://feeds.bloomberg.com/markets/news.rss"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)

# حالت دستی (کامند /news)
async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(await get_news_text())

# حالت دستی (کامند /start)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to BloombergFarsiBot!\nUse /live to watch Bloomberg Live.\nUse /news to get latest Bloomberg headlines."
    )

# تابع دریافت اخبار
async def get_news_text():
    feed = feedparser.parse(BLOOMBERG_FEED)
    if not feed.entries:
        return "No news found from Bloomberg."

    messages = ["📰 Latest Bloomberg Headlines:"]
    for entry in feed.entries[:8]:
        messages.append(f"• {entry.title}\n{entry.link}")
    return "\n\n".join(messages)

# تابع ارسال اتوماتیک برای کران
async def send_news_auto():
    logging.info("📤 Sending Bloomberg news automatically...")
    text = await get_news_text()
    await bot.send_message(chat_id=CHANNEL_ID, text=text)

# تابع اصلی
async def main():
    if len(sys.argv) > 1 and sys.argv[1] == "cron":
        await send_news_auto()
    else:
        app = ApplicationBuilder().token(BOT_TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("news", news))
        await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
