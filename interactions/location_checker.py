from telegram import Update
from interactions.helpers import distance
from location_list import LOCATION1

def check_location(update:Update):
    latitude = update.message.location.latitude
    longitude = update.message.location.longitude
    print(latitude)
    print(longitude)
    if distance(latitude, longitude, LOCATION1["latitude"], LOCATION1["longitude"]) < 150:
        return True
    return False
