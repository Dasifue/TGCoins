
# Crypto Telegram Bot

Этот проект представляет собой Telegram-бота для работы с криптовалютами, использующего CoinGecko API для получения информации о текущих ценах и другой статистике.

## Установка

1. Клонируйте репозиторий на ваш локальный компьютер:

   ```bash
   git clone https://github.com/your-username/crypto-telegram-bot.git
   cd crypto-telegram-bot
   ```

2. Установите зависимости, указанные в `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

## Конфигурация

Для работы бота потребуется Telegram токен. Зарегистрируйте своего бота у [@BotFather](https://core.telegram.org/bots#botfather) и получите токен.

Создайте файл `.env` в корневой директории проекта и добавьте ваш токен:

   ```plaintext
   TELEGRAM_TOKEN=ваш_телеграм_токен
   ```

## Запуск

После установки всех зависимостей и настройки конфигурации, вы можете запустить проект:

   ```bash
   python coin.py
   ```

## Описание работы

- **CoinGecko API**: Используется для получения данных о ценах, рыночной капитализации и другой информации о криптовалютах.
- **Telegram Bot**: Бот принимает команды от пользователей, такие как запросы на текущие цены криптовалют и другие данные.

## Использование

- Отправьте `/start` боту, чтобы начать взаимодействие.
- Запросите информацию о криптовалютах с помощью команды `/price <имя_криптовалюты>`.

## Лицензия

Этот проект распространяется под лицензией MIT.