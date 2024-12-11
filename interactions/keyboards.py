from telegram import ReplyKeyboardMarkup, KeyboardButton


# Generate Main Keyboard
def start_keyboard():
    keyboard = [
        ["Начать смену"],
    ]
    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Выберите вариант",
    )
    return reply_markup

# Ask user for location
def location_keyboard():
    keyboard = [
        [KeyboardButton("Отправить локацию", request_location=True)]
    ]
    reply_markup = ReplyKeyboardMarkup(
    keyboard,
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Отправить локацию",)
    return reply_markup