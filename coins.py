"Module for CoinGecko API"

import asyncio
import os
from typing import Any

import aiohttp
from dotenv import load_dotenv


load_dotenv()

API_TOKEN = os.getenv("API_TOKEN", "token")


async def get_data(url: str, token: str) -> list[dict[str, Any]]:
    "Функция отправляет запрос и возвращает json данные"
    headers = {
        "x-cg-api-key": token
    }
    async with aiohttp.ClientSession() as session:
        response = await session.get(url=url, headers=headers)
        return await response.json()


async def get_id_and_name(data: list[dict[str, Any]]) -> list[dict[str, Any]]:
    "Функция парсит данные и возвращает id & name каждой крипты"
    result = []
    for coin in data:
        result.append(
            {
                "id": coin["id"],
                "name": coin["name"]
            }
        )
    return result


async def main():
    "Main function"
    data = await get_data(
        url="https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd",
        token=API_TOKEN
    )
    id_names = await get_id_and_name(data=data)
    print(id_names)

asyncio.run(main())
