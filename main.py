import os
import asyncio
import datetime
import time
import logging
from aiogram import Dispatcher, Bot, executor # 2.5.1 version, 3 is a trash
from get_image import url

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

line_length = 100
line = "~" * line_length


# Put your values in a virtual environment
token = str(os.getenv("TELEGRAM_BOT_TOKEN"))
channel_id = int(str(os.getenv("CHANNEL_ID")))

logger.debug("sleep to prevent bugs")
time.sleep(10)

bot = Bot(token)
dp = Dispatcher(bot)
os.system('clear')

logger.info("bot object is created")
async def send_post():

    cat_url = str(url())
    await bot.send_photo(channel_id, cat_url)
    logger.info(f"bot is sended a {cat_url} pic.")
    logger.info(f"bot is going to sleep.")


async def scheduler(): 
    while True:
        now = datetime.datetime.now()
        if now.minute == 19:
            try:
                await send_post()
                await asyncio.sleep(60) # To prevent spam 

            except Exception as e:
                logger.info('\n' + line + '\n' + "bot is cached an error: "
                    + str(e) + '\n' + line)
                await send_post()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(scheduler())
    time.sleep(10)
    executor.start_polling(dp, skip_updates=True)
