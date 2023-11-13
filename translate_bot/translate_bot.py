import logging
import time

from telegram import (
    Update,
    Message,
)
from telegram.ext import (
    CommandHandler,
    CallbackContext,
    Updater,
    MessageHandler,
    Filters,
    JobQueue           ,
)

import bot_settings

WELCOME_TEXT = (
    "Type a number to get messages with the specified amount of delay between them."
)

logging.basicConfig(
    format="[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    logger.info(f"> Start chat #{chat_id}")
    context.bot.send_message(
        chat_id=chat_id,
        text=WELCOME_TEXT,
    )


def on_text(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    msg = update.message.text
    logger.info(f"+ Got #{chat_id}: {msg!r}")
    try:
        v = int(msg)
    except ValueError:
        context.bot.send_message(chat_id=chat_id, text="???")
        return

    m: Message = context.bot.send_message(
        chat_id=chat_id, text=f"Waiting for {v} seconds..."
    )
    jq.run_once(after_rest, v, m)


def after_rest(context: CallbackContext):
    m: Message = context.job.context
    m.reply_text("Done.", quote=True)


my_bot = Updater(token=bot_settings.BOT_TOKEN, use_context=True)
jq: JobQueue = my_bot.job_queue

my_bot.dispatcher.add_handler(CommandHandler("start", start))
my_bot.dispatcher.add_handler(MessageHandler(Filters.text, on_text))


logger.info("* Start polling...")
my_bot.start_polling()  # Starts polling in a background thread.
my_bot.idle()  # Wait until Ctrl+C is pressed
logger.info("* Bye!")
