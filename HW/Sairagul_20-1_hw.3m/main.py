from aiogram import types
from aiogram.utils import executor
import config

@config.dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    question = "В каком году Эйнштейн получил Нобелевскую премию?"
    answers = [
        "1915"
        "1905"
        "1916"
        "1930"
        "1921"
    ]
    await config.bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=4
    )

@config.dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await config.bot.send_message(message.from_user.id,
                           f"Salam {message.from_user.full_name}")

@config.dp.message_handler()
async def echo(message: types.Message):
    await config.bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    executor.start_polling(config.dp, skip_updates=True)
