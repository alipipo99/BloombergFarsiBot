# BloombergFarsiBot - اخبار انگلیسی از بلومبرگ با پخش زنده

import logging
import feedparser
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ---------------- تنظیمات اصلی ----------------
BOT_TOKEN = "7687238301:AAGXMxVR4EDlR284kM4SdDCoEtPZoIMVZb8"
BLOOMBERG_FEED = "https://feeds.bloomberg.com/markets/news.rss"
LIVE_URL = "https://www.youtube.com/@Bloomberg/live"
CHANNEL_ID = "-1002006111361"

# ---------------- تنظیمات لاگ ----------------
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ---------------- دستور /start ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to BloombergFarsiBot!\nUse /live to watch Bloomberg Live.\nUse /news to get latest Bloomberg headlines."
    )

# ---------------- دستور /live ----------------
async def live(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"📺 Bloomberg Live:\n{LIVE_URL}")

# ---------------- دستور /news ----------------
async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    feed = feedparser.parse(BLOOMBERG_FEED)
    if not feed.entries:
        await update.message.reply_text("No news found from Bloomberg.")
        return

    messages = ["📰 Latest Bloomberg Headlines:"]
    for entry in feed.entries[:10]:
        messages.append(f"• {entry.title}\n{entry.link}")

    text = "\n\n".join(messages)
    await context.bot.send_message(chat_id=CHANNEL_ID, text=text)

# ---------------- راه‌اندازی ربات ----------------
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("live", live))
    app.add_handler(CommandHandler("news", news))
    app.run_polling()

if __name__ == '__main__':
    main()
