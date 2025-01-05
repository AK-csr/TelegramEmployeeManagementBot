from telegram import Update
import pytz
from config import MY_TIMEZONE
from googlesheets.sheets import accessWorkerSheet

def get_message_info(update: Update):
    user = update.message.from_user
    first_name = user.first_name
    last_name = user.last_name
    username = user.username
    tz = pytz.timezone(MY_TIMEZONE)
    message_time = update.message.date.now(tz).strftime('%Y-%m-%d %H:%M:%S')
    new_row = [first_name, last_name, username, message_time]
    sheet = accessWorkerSheet()
    sheet.append_row(new_row, value_input_option="USER_ENTERED")


def get_location(update:Update):
    latitude = update.message.location.latitude
    longitude = update.message.location.longitude
    f = open("info.txt", "a")
    f.write(f"Location: {latitude} {longitude}")
    f.close