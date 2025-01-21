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

    # Получение фото пользователя
    photo_url = "https://cdn-icons-png.flaticon.com/512/847/847969.png"  # Фото по умолчанию
    photos = await bot.get_user_profile_photos(user_id)

    if photos.photos:
        # Получаем URL фото
        file_id = photos.photos[0][-1].file_id
        file = await bot.get_file(file_id)
        photo_url = f"https://api.telegram.org/file/bot{bot.token}/{file.file_path}"

    # Добавление параметра версии в URL
    version_param = f"?v={int(time.time())}"
    url = f'https://wwersder.github.io/alitabot/index.html{version_param}&photo={photo_url}'

    # Создание кнопки с веб-приложением
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='GAME', web_app=WebAppInfo(url=url))]
        ]
    )

    await message.answer('Ссылка на DEV приложение алиты 👇', reply_markup=markup)


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())