import feedparser
import logging
from telegram import Bot

# تنظیمات ربات
BOT_TOKEN = "7687238301:AAGXMxVR4EDlR284kM4SdDCoEtPZoIMVZb8"
CHANNEL_ID = "-1002006111361"
BLOOMBERG_RSS = "https://feeds.bloomberg.com/markets/news.rss"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)

def send_news():
    feed = feedparser.parse(BLOOMBERG_RSS)
    if not feed.entries:
        logging.warning("No news entries found.")
        return

    messages = ["📰 Latest Bloomberg Headlines:"]
    for entry in feed.entries[:8]:
        messages.append(f"• {entry.title}\n{entry.link}")

    text = "\n\n".join(messages)
    bot.send_message(chat_id=CHANNEL_ID, text=text)
    logging.info("✅ News sent to Telegram channel.")

if __name__ == "__main__":
    send_news()
