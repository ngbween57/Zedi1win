
import loggin
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

API_TOKEN = 7678926004:AAFbiUskAC18GjYXPkZ_7apvNwoF5RUGhLI

# Logging setup
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Custom keyboard
menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.add(KeyboardButton("Signal olish"))

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Salom! Bu bot Mines o'yini uchun random signal yuboradi.",
        reply_markup=menu_keyboard
    )

@dp.message_handler(lambda message: message.text == "Signal olish")
async def send_signal(message: types.Message):
    # 1dan 25gacha bo'lgan random 3ta katak tanlaymiz
    signal_cells = random.sample(range(1, 26), 3)
    cells_str = ", ".join(map(str, signal_cells))
    await message.answer(f"Tavsiya etilgan xavfsiz kataklar: {cells_str}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
