# BloombergFarsiBot - اخبار انگلیسی از بلومبرگ به صورت خودکار و دستی

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import feedparser
import asyncio
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")
BLOOMBERG_FEED = "https://feeds.bloomberg.com/markets/news.rss"
LIVE_URL = "https://www.youtube.com/@Bloomberg/live"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to BloombergFarsiBot!\nUse /live to watch Bloomberg Live.\nUse /news to get latest Bloomberg headlines."
    )

async def live(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"📺 Bloomberg Live:\n{LIVE_URL}")

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_news(context.bot)

async def send_news(bot):
    feed = feedparser.parse(BLOOMBERG_FEED)
    if not feed.entries:
        return

    messages = ["📰 Latest Bloomberg Headlines:"]
    for entry in feed.entries[:10]:
        messages.append(f"• {entry.title}\n{entry.link}")

    await bot.send_message(chat_id=CHANNEL_ID, text="\n\n".join(messages))

async def auto_news(context: ContextTypes.DEFAULT_TYPE):
    while True:
        try:
            await send_news(context.bot)
        except Exception as e:
            logging.error(f"Error sending news: {e}")
        await asyncio.sleep(3 * 60 * 60)  # 3 hours

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("live", live))
    app.add_handler(CommandHandler("news", news))

    # اجرای اتوماتیک همزمان
    asyncio.create_task(auto_news(app.bot))

    print("✅ BloombergFarsiBot is running...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
