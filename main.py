from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import asyncio
import time

bot = Bot('7878345097:AAGArCEZCN2Q1_DVYdKtEM-XwMadYgps9bI')
dp = Dispatcher()
router = Router()

@router.message(F.text == '/start')
async def start(message: Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    user_photo = message.from_user.photo

    if user_photo:
        photo_url = await bot.get_user_profile_photos(user_id)
        if photo_url.photos:
            user_photo_url = photo_url.photos[0][-1].file_id
            user_photo_url = await bot.get_file(user_photo_url)
            photo_url = f"https://api.telegram.org/file/bot{bot.token}/{user_photo_url.file_path}"
        else:
            photo_url = "https://cdn-icons-png.flaticon.com/512/847/847969.png"
    else:
        photo_url = "https://cdn-icons-png.flaticon.com/512/847/847969.png"

    version_param = f"?v={int(time.time())}"
    url = f'https://wwersder.github.io/alitabot/index.html{version_param}&photo={photo_url}'

    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='GAME', web_app=WebAppInfo(url=url))]
        ],
        resize_keyboard=True
    )

    await message.answer('Ссылка на DEV приложение алиты 👇', reply_markup=markup)

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())