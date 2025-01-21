from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
import asyncio
import time

bot = Bot('7878345097:AAGArCEZCN2Q1_DVYdKtEM-XwMadYgps9bI')
dp = Dispatcher()
router = Router()

@router.message(F.text == '/start')
async def start(message: Message):
    version_param = f"?v={int(time.time())}"
    url = f'https://wwersder.github.io/alitabot/index.html{version_param}'

    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='zaxodi', web_app=WebAppInfo(url=url))]
        ],
        resize_keyboard=True
    )

    await message.answer('link nize', reply_markup=markup)

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())