from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
import asyncio

bot = Bot('7878345097:AAGArCEZCN2Q1_DVYdKtEM-XwMadYgps9bI')
dp = Dispatcher()
router = Router()

@router.message(F.text == '/start')
async def start(message: Message):
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='zaxodi', web_app=WebAppInfo(url='https://wwersder.github.io/alitabot/index.html'))]
        ],
        resize_keyboard=True
    )
    await message.answer('link nize', reply_markup=markup)

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())