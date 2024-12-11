from telegram import Update
import pytz
from config import MY_TIMEZONE

def get_message_info(update: Update):
    user = update.message.from_user
    first_name = user.first_name
    last_name = user.last_name
    username = user.username
    tz = pytz.timezone(MY_TIMEZONE)
    message_time = update.message.date
    f = open("info.txt", "w")
    f.write(f"Имя: {first_name} {last_name}\n Username: {username} \n Время: {message_time.now(tz).strftime('%Y-%m-%d %H:%M:%S')} \n")
    f.close()

def get_location(update:Update):
    latitude = update.message.location.latitude
    longitude = update.message.location.longitude
    f = open("info.txt", "a")
    f.write(f"Location: {latitude} {longitude}")
    f.close