import os
import asyncio
import datetime
import time
import logging
from aiogram import Dispatcher, Bot, executor # 2.5.1 version, 3 is a trash
from get_image import url

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Put your values in a virtual environment
token = str(os.getenv("TELEGRAM_BOT_TOKEN"))
channel_id = int(str(os.getenv("CHANNEL_ID")))

logger.debug("sleep to prevent bugs")
time.sleep(5)

bot = Bot(token)
dp = Dispatcher(bot)
logger.info("bot object is created")

async def send_post():

    cat_url = str(url())
    await bot.send_photo(channel_id, cat_url)
    logger.info(f"bot sended a {cat_url} pic.")
    logger.info(f"bot is going to sleep.")


async def scheduler(): 
    while True:
        now = datetime.datetime.now()
        if now.minute == 19:
            try:
                await send_post()

            except Exception as e:
                logger.error(e)
                await send_post()

        await asyncio.sleep(60) # To prevent spam 

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(scheduler())
    time.sleep(5)
    executor.start_polling(dp, skip_updates=True)
