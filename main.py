"Основной выполняемый модуль программы"

import os
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from coins import get_data, get_id_and_name

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN", "token")
BOT_TOKEN = os.getenv("BOT_TOKEN", "bot token")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message) -> None:
    "Функция отвечает на команду /start и приветствует пользователя"
    text = f"Hello, {message.from_user.username}!" # type: ignore
    markup = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="Info", callback_data="info"),
        InlineKeyboardButton(text="Coins", callback_data="coins")
    ]])
    await message.answer(text=text, reply_markup=markup)


@dp.callback_query(lambda call: call.data == "info")
async def get_info(call: CallbackQuery) -> None:
    "Функиця отправляет информацию о боте"
    await call.message.answer(text="Some info!")  # type: ignore


@dp.callback_query(lambda call: call.data == "coins")
async def get_coins_list(call: CallbackQuery) -> None:
    "Функция отправляет пользователю список криптовалюты"
    data = await get_data(
        url="https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&per_page=10",
        token=API_TOKEN
    )
    id_and_name = await get_id_and_name(data=data)
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=coin['name'], callback_data=f"id:{coin['id']}")]
        for coin in id_and_name
    ])
    text = "Here some coins!"
    await call.message.answer(text=text, reply_markup=markup)  # type: ignore 


@dp.callback_query(lambda call: call.data.startswith("id:"))
async def get_coin_data(call: CallbackQuery) -> None:
    "Функция возвращает информацию о крипте"
    coin_id = call.data[3:]  # type: ignore
    url = "https://api.coingecko.com/api/v3/coins/" + coin_id
    data = await get_data(url=url, token=API_TOKEN)
    text = f"{data['name']}: ${data['market_data']['current_price']['usd']}"  # type: ignore
    await call.message.answer_photo(photo=data['image']['large'], caption=text)  # type: ignore


async def main() -> None:
    "Функция запускает бота и всю программу"
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
