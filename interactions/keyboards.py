from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


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

def choose_location():
    keyboard = [
        [
        InlineKeyboardButton("Локация 1", callback_data="loc1"),
        InlineKeyboardButton("Локация 2", callback_data="loc2")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup