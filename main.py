from typing import Final
import config
from interactions.keyboards import (start_keyboard, location_keyboard)
from interactions.get_message_info import (get_message_info, get_location)
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

MY_TIMEZONE = config.MY_TIMEZONE
TOKEN: Final = config.TOKEN
BOT_USERNAME: Final = config.BOT_USERNAME

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # Send a message with a keyboard
    await update.message.reply_text(
        "Выберите вариант:",
        reply_markup=start_keyboard()
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This bot helps with employee management")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Custom Command")

# Replies

def handle_response(text:str) -> str:
    proccessed:str = text.lower()
    if 'начать смену' in proccessed:
        return "Удачного дня"
    
    return "No command found"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    get_message_info(update)
    text:str = update.message.text

    print(f'User ({update.message.chat.id}): "{text}"')
    response: str = handle_response(text)

    await update.message.reply_text(response, reply_markup=location_keyboard())

async def location_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    get_location(update)

    await update.message.reply_text("Ваша локация отправлена")

# Errors

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update{update} caused error{context.error}')

if __name__ == '__main__':
    #Initialize
    print("Starting up....")
    app = Application.builder().token(TOKEN).build()
    print("Bot Running....")

    #Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    #Replies
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_handler(MessageHandler(filters.LOCATION, location_message))

    #Errors
    app.add_error_handler(error)

    print("Polling...")
    app.run_polling(poll_interval=5)