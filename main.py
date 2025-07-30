import os
import asyncio
from telegram import Bot
from telegram.ext import ApplicationBuilder, ContextTypes
import feedparser

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
RSS_URL = "https://www.bloomberg.com/feed/podcast/etf-report.xml"

async def send_news():
    bot = Bot(token=BOT_TOKEN)
    feed = feedparser.parse(RSS_URL)
    for entry in feed.entries[:3]:
        title = entry.title
        link = entry.link
        published = entry.published
        message = f"{title}\n{link}\n{published}"
        await bot.send_message(chat_id=CHAT_ID, text=message)

async def main():
    await send_news()

if __name__ == "__main__":
    asyncio.run(main())
