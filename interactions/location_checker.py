from telegram import Update
import sys

sys.path.append('../telegrambot')

from location_list import LOCATION1
from math import cos, asin, sqrt, pi

def distance(lat1, lon1, lat2, lon2):
    r = 6371
    p = pi / 180

    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return (2 * r * asin(sqrt(a)))*1000


def check_location(update:Update):
    latitude = update.message.location.latitude
    longitude = update.message.location.longitude
    print(distance(latitude, longitude, LOCATION1[latitude], LOCATION1[longitude]))