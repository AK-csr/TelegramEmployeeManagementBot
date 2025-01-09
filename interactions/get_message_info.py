import sys

sys.path.append('../telegrambot')
from telegram import Update
from interactions.helpers import find_last_row
import pytz
from config import MY_TIMEZONE
from googlesheets.sheets import accessWorkerSheet

# Saves the user start data to the database
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

# Saves user end time to the database
def get_shift_end(update:Update):
    name = update.message.from_user.first_name
    tz = pytz.timezone(MY_TIMEZONE)
    message_time = update.message.date.now(tz).strftime('%Y-%m-%d %H:%M:%S')
    sheet = accessWorkerSheet()
    found_rows = sheet.findall(name)
    last_row = find_last_row(found_rows)
    sheet.update_cell(last_row, 5, message_time)
