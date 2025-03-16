import asyncio
from tg_bot.bot.bot import start_bot

if __name__ == "__main__":
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        print("\n___Bot Finished___")
