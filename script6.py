import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties  # ← Добавлен импорт
from aiogram.types import ChatJoinRequest

# Ваши данные
BOT_TOKEN = "6088662691:AAFBkynSsVzggnurUOiZ6xqJGCdyqsmFXfU"
CHANNEL_ID = -1001660061515  # ID вашего канала

async def approve_request(chat_join: ChatJoinRequest, bot: Bot):
    try:
        await chat_join.approve()
        await bot.send_message(
            chat_id=chat_join.from_user.id,
            text="✅ Заявка одобрена! Добро пожаловать в канал.
            https://t.me/+NJWfkT3Mjlk0NzBi"
        )
        logging.info(f"Одобрена заявка от {chat_join.from_user.id}")
    except Exception as e:
        logging.error(f"Ошибка при одобрении заявки: {e}")

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )

    # Инициализация бота с новыми настройками
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode="HTML")  # ← Исправленный синтаксис
    )
    dp = Dispatcher()

    # Регистрируем обработчик заявок
    dp.chat_join_request.register(
        approve_request,
        F.chat.id == CHANNEL_ID
    )

    logging.info("Бот запущен. Ожидание заявок...")
    await dp.start_polling(bot)

if __name__ == "__main__":

    asyncio.run(main())
