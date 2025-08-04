# 📰 News Aggregator Telegram Bot

Бот для поиска новостей с Habr, BBC и РБК с удобным интерфейсом и пагинацией.

## 🌟 Особенности
- Интерактивное меню с inline-кнопками
- Поиск по нескольким источникам (Habr, BBC, РБК)
- Пагинация новостей (листание кнопками)
- Кеширование запросов (на 3 часа)
- Обработка ошибок и логирование

## 🛠 Технологии
- Python 3.10+
- Aiogram 3.x
- BeautifulSoup4 (парсинг)
- CacheTools (кеширование)

## ⚡️ Быстрый старт

1. Клонируйте репозиторий:
***bash
git clone https://github.com/ваш-репозиторий/news-bot.git
cd news-bot

2. Установите зависимости:

pip install -r requirements.txt

3. Настройте бота:

* Получите токен у @BotFather

* Вставьте его в config.py:
TELEGRAM_BOT_TOKEN = "ваш_токен"

4. Запустите бота:

python bot.py

