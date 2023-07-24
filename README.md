# Telegram GPT-4 Chatbot

### Description:
This is a Telegram bot that interacts with users to generate text using OpenAI's GPT-4 model.  
The bot takes user input and replaces default data in the GPT-4 prompt template.  
Based on the modified prompt, it obtains the generated text from GPT-4 and sends it back to the user. 

### Features:

- Interact with the bot by sending messages.
- The bot uses GPT-4 to generate text based on user input.
- Provides a warm welcome message on the "/start" command.
- Handles exceptions gracefully and responds with appropriate error messages.



### Installation

1. Clone the repo
`git clone https://github.com/oksanaaam/chatGPT4_prompt_tg_bot.git`
2. Open the project folder in your IDE
3. Open a terminal in the project folder
4. If you are using PyCharm - it may propose you to automatically create venv for your project and install requirements in it, but if not:
```
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```


### Set the environment and get an API key.
Set the required environment variables in .env.sample file:

Set up a Telegram bot and obtain the Telegram bot token.  
Obtain the OpenAI API key for GPT-4 access.

```
OPENAI_API_KEY = <your OPENAI_API_KEY>
TELEGRAM_BOT_TOKEN = <your TELEGRAM_BOT_TOKEN>
```

Run the `bot.py` script to start the Telegram bot.  
Chat with the bot by sending messages, and it will generate responses based on GPT-4.


### Testing:
The code includes two test cases:

- test_handle_message_exception: This tests the handle_message function when an exception occurs during the GPT-4 text generation process.   
It checks if the bot handles the error and replies with an appropriate error message.

- test_on_start: This tests the on_start function, which handles the "/start" command.   
It verifies if the bot sends a welcome message when a user starts a chat.

To run the tests, execute the `python tests.py` command in the project directory.

Some photo to see how chat look like:

Start chating
![chating.png](images%20for%20README.md%2Fchating.png)

Running bot 
![running_bot.png](images%20for%20README.md%2Frunning_bot.png)
