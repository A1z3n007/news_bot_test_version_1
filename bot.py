import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from parsers.habr import get_habr_news
from parsers.bbc import get_bbc_news
from parsers.rbk import get_rbk_news
from utils.cache import get_cached_news
from config import config

bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

def get_sources_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(text="Habr", callback_data="source_habr"),
        types.InlineKeyboardButton(text="BBC", callback_data="source_bbc"),
        types.InlineKeyboardButton(text="РБК", callback_data="source_rbk"),
    )
    return builder.as_markup()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🔍 Привет! Я новостной бот.\n"
        "• Напиши /news [запрос] — поиск по всем источникам.\n"
        "• Или выбери источник:",
        reply_markup=get_sources_keyboard(),
    )

@dp.message(Command("news"))
async def news_all(message: types.Message):
    query = message.text.split(maxsplit=1)[1] if len(message.text.split()) > 1 else "IT"
    results = []
    for source in ["habr", "bbc", "rbk"]:
        news = get_cached_news(source, query, globals()[f"get_{source}_news"])
        results.extend(news)
    await message.answer("\n\n".join(results[:10]))

@dp.message(Command("news_habr", "news_bbc", "news_rbk"))
async def news_source(message: types.Message):
    command = message.text.split("_")[1].split()[0]
    query = message.text.split(maxsplit=1)[1] if len(message.text.split()) > 1 else "IT"
    news = get_cached_news(command, query, globals()[f"get_{command}_news"])
    await message.answer("\n\n".join(news))

@dp.callback_query(F.data.startswith("source_"))
async def handle_source(callback: types.CallbackQuery):
    source = callback.data.split("_")[1]
    await callback.message.answer(f"Напиши запрос для поиска в {source.upper()}:")

if __name__ == "__main__":
    dp.run_polling(bot)