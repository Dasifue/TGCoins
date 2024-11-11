"Module for CoinGecko API"

from typing import Any

import aiohttp

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
