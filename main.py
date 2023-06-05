import telegram
from telegram.ext import CommandHandler, Updater
import json
import os
from dotenv import load_dotenv


load_dotenv()


TOKEN = os.getenv("TOKEN")


import telegram
from telegram.ext import CommandHandler, Updater
from bs4 import BeautifulSoup
import json
import os
from dotenv import load_dotenv


load_dotenv()


TOKEN = os.getenv("TOKEN")




def fetchGames(update, context):
    file_path = "week1.json"

    with open(file_path, "r") as file:
        json_data = json.load(file)

    games = json_data["games"]
    messages = []

    for game in games:
        name = game["name"]
        store = game["store"]
        duration = game["duration"]
        url = game["url"]

        message = f"Name: {name}\nStore: {store}\nDuration: {duration}\nURL: {url}"
        messages.append(message)

    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="\n\n".join(messages))





def main():
    # Set up the bot
    updater = Updater(token=TOKEN,use_context=True)
    dispatcher = updater.dispatcher

    # Register the command handler
    new_handler = CommandHandler('new', fetchGames)
    dispatcher.add_handler(new_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()