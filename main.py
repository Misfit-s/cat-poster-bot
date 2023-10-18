import os
import asyncio
import datetime
from aiogram import Dispatcher, Bot, executor
from get_image import url

# Put your values in a virtual environment
token = str(os.getenv("TELEGRAM_BOT_TOKEN"))
channel_id = int(str(os.getenv("CHANNEL_ID")))

bot = Bot(token)
dp = Dispatcher(bot)

async def send_post():

    cat_url = str(url())
    await bot.send_photo(channel_id, cat_url)


async def scheduler(): 
    while True:
        now = datetime.datetime.now()
        if now.minute == 19:
            await send_post()

        await asyncio.sleep(60) # To prevent spam 

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(scheduler())
    executor.start_polling(dp, skip_updates=True)
