from telegram import Bot, ParseMode
from telegram.ext import CommandHandler, Updater
import json
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

def searchGames():
    #query = " ".join(context.args)
    query = "GTAV"
    #if not query:
     #   context.bot.send_message(chat_id=update.effective_chat.id, text="Please Enter A Game")
      #  return
    
    search_url = f"https://www.g2a.com/search?query={query}"

    response = requests.get(search_url)

    soup = BeautifulSoup(response.txt,"html.parser")


    print(soup)



searchGames()