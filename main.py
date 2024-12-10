from typing import Final
import pytz
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

MY_TIMEZONE = "Asia/Almaty"
TOKEN: Final = "7066427661:AAHszSRbR5R33SNtYMFdaye9Z3SKUg5MkDs"
BOT_USERNAME: Final = "@ak_private_workbot"

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Menu Keyboard
    keyboard = [
        ["Начать смену"],
    ]
    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Выберите вариант",
    )

    # Send a message with a keyboard
    await update.message.reply_text(
        "Выберите вариант:",
        reply_markup=reply_markup
    )

async def request_location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("Начать смену", request_location=True)]
    ]
    reply_markup = ReplyKeyboardMarkup(
    keyboard,
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Начать смену",)

    await update.message.reply_text(
    "Share your Location",
    reply_markup=reply_markup)

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
    text:str = update.message.text
    user = update.message.from_user
    first_name = user.first_name
    last_name = user.last_name
    username = user.username
    tz = pytz.timezone(MY_TIMEZONE)
    message_time = update.message.date
    f = open("info.txt", "w")
    f.write(f"Имя: {first_name} {last_name}\n Username: {username} \n Время: {message_time.now(tz).strftime('%Y-%m-%d %H:%M:%S')} \n")
    f.close()

    if update.message.location:
        latitude = update.message.location.latitude
        longitude = update.message.location.longitude
        f = open("info.txt", "a")
        f.write(f"Location: {latitude} {longitude}")
        f.close

    print(f'User ({update.message.chat.id}): "{text}"')
    response: str = handle_response(text)

    await update.message.reply_text(response)

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
    app.add_handler(CommandHandler('location', request_location))

    #Replies
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #Errors
    app.add_error_handler(error)

    print("Polling...")
    app.run_polling(poll_interval=5)