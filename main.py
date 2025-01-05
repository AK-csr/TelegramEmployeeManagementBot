from typing import Final
import config
from interactions.keyboards import (start_keyboard, location_keyboard, choose_location)
from interactions.get_message_info import (get_message_info, get_location)
from interactions.location_checker import (check_location)
from googlesheets.sheets import (accessWorkerSheet)
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
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

#  Choose Location 
async def location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    context.user_data["selected_location"] = query.data

    await query.edit_message_text(
        text=f"Вы выбрали {query.data}. Отправьте вашу локацию:"
    )
    await query.message.reply_text("Нажмите чтобы отправить вашу локацию:", reply_markup=location_keyboard())


#   Start command message
def handle_response(text:str) -> str:
    proccessed:str = text.lower()
    if 'начать смену' in proccessed:
        return "Выберите место работы"
    

    return "No command found"

#   Start command logic
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    get_message_info(update)
    text:str = update.message.text

    print(f'User ({update.message.chat.id}): "{text}"')
    response: str = handle_response(text)

    await update.message.reply_text(response, reply_markup=choose_location())

#   Location handler
async def location_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    get_location(update)
    check_location(update)

    user_location = update.message.location
    selected_location = context.user_data.get("selected_location")

    if not user_location or not selected_location:
        await update.message.reply_text("Something went wrong. Please start again.")
        return
    
    await update.message.reply_text(
    f"You selected {selected_location}. "
    f"Your current location is:\nLatitude: {user_location.latitude}, Longitude: {user_location.longitude}.\n"
    "You can now process further!"
    )
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
    app.add_handler(CallbackQueryHandler(location))

    #Errors
    app.add_error_handler(error)

    print("Polling...")
    app.run_polling(poll_interval=5)
