import pytest
from aiogram import types
from bot import handle_message, on_start
from unittest.mock import AsyncMock, patch


@pytest.fixture
def update():
    return types.Message()


@patch("openai.Completion.create", side_effect=Exception("An error occurred"))
@pytest.mark.asyncio
async def test_handle_message_exception(mock_create, update):
    user_input = "Your user input here"
    update.text = user_input

    update.reply = AsyncMock()

    await handle_message(update)

    mock_create.assert_called_once_with(
        engine="text-davinci-002",
        prompt=user_input + "?",
        max_tokens=250,
        temperature=0.7
    )

    update.reply.assert_called_once_with(
        "An error occurred while processing your request. Please try again later."
    )


@patch("aiogram.Bot.send_message")
@pytest.mark.asyncio
async def test_on_start(mock_send_message, update):
    user_id = 123456789
    update.from_user = types.User(id=user_id)

    mock_send_message.return_value = None

    await on_start(update)

    mock_send_message.assert_called_once_with(
        chat_id=user_id,
        text="Hello, I am chat GPT 4 bot. What is your question?"
    )
