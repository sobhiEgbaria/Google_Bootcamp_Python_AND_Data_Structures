import logging
import requests
import json

from telegram import Update
from telegram.ext import (
    CommandHandler,
    CallbackContext,
    MessageHandler,
    filters,
    Updater,
)

import bot_settings

logging.basicConfig(
    format="[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


# def Nearby_Search():
#     url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=suhsi&location=-33.8670522%2C151.1957362&radius=1500&type=restaurant&key={GOOGLE_API_KEY}"
#     res = requests.get(url).json()
#     result_details = {}
#     for i in res["results"]:
#         result_details[i["name"]] = [i["geometry"]["location"], i["photos"]]

#     print(result_details)


# Nearby_Search()


def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    logger.info(f"> Start chat #{chat_id}")
    context.bot.send_message(chat_id=chat_id, text="hi this is sobhi from home")


def respond(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    text = update.message.text
    logger.info(f"= Got on chat #{chat_id}: {text!r}")
    response = text.replace("7", "💣")
    context.bot.send_message(chat_id=update.message.chat_id, text=age_of_celb(response))


my_bot = Updater(token=bot_settings.BOT_TOKEN, use_context=True)
my_bot.dispatcher.add_handler(CommandHandler("start", start))
my_bot.dispatcher.add_handler(MessageHandler(filters.text, respond))

logger.info("* Start polling...")
my_bot.start_polling()  # Starts polling in a background thread.
my_bot.idle()  # Wait until Ctrl+C is pressed
logger.info("* Bye!")
