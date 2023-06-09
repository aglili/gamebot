# -*- coding: utf-8 -*-
from telegram import Bot, ParseMode
from telegram.ext import CommandHandler, Updater
import json
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()

TOKEN = os.getenv("TOKEN")
RENDER_URL = os.getenv("RENDER_URL")
DEPLOY_HOOK = os.getenv("DEPLOY_HOOK")

bot = Bot(token=TOKEN)


def startMessage(update, context):
    message = """\
    *Hello!* 👋
    I'm the Telegram Game Bot, your companion for finding free games! 🎮🆓

    *How to Use:*
    1. Use the `/new` command to get a list of available games.
    2. Each game will be displayed with its name, store, duration, and URL.
    3. Click on the URL to visit the store and grab the game for free!

    Feel free to explore the list and enjoy gaming! If you have any questions or need assistance, just let me know.

    Happy gaming! 🎉🕹️
    """
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.MARKDOWN)


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


def fetchDeals(update, context):
    file_path = "deal1.json"

    with open(file_path, "r") as file:
        json_data = json.load(file)

    games = json_data["deals"]
    messages = []

    for game in games:
        name = game["name"]
        store = game["store"]
        duration = game["duration"]
        price_changes = game["was-now"]
        url = game["url"]

        message = f"Name: {name}\nStore: {store}\nPriceChanges: {price_changes}\nDuration: {duration}\nURL: {url}"
        messages.append(message)

    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="\n\n".join(messages))









def main():
    # Set up the bot
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register the command handlers
    new_handler = CommandHandler('new', fetchGames)
    start_handler = CommandHandler('start', startMessage)
    deal_handler = CommandHandler('deal',fetchDeals)
    dispatcher.add_handler(new_handler)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(deal_handler)
    # Start the bot
    updater.start_webhook(listen="0.0.0.0", port=80, url_path=TOKEN,webhook_url = f"{RENDER_URL}/{TOKEN}")
    updater.idle()


if __name__ == '__main__':
    main()
