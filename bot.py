import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
import openai
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


async def handle_message(update: types.Message):
    user_input = update.text.strip()

    openai.api_key = OPENAI_API_KEY

    end_of_sentence = user_input.endswith((".", "!", "?"))

    prompt = user_input if end_of_sentence else user_input + "?"

    try:
        generated_text = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=250,
            temperature=0.7
        )
        if generated_text and generated_text.choices:
            await update.reply(generated_text.choices[0].text)
        else:
            await update.reply("Sorry, I couldn't generate a response at the moment.")
    except Exception as e:
        logging.error(f"Error in handle_message: {e}")
        await update.reply("An error occurred while processing your request. Please try again later.")


async def on_start(update: types.Message):
    user_id = update.from_user.id
    await bot.send_message(chat_id=user_id, text="Hello, I am chat GPT 4 bot. What is your question?")


async def on_message(update: types.Message):
    if update.text.strip().lower() != "/start":
        await handle_message(update)


def main():
    dp.register_message_handler(on_start, commands=["start"])
    dp.register_message_handler(on_message)

    executor.start_polling(dp)


if __name__ == "__main__":
    main()
