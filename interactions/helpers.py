from math import cos, asin, sqrt, pi

# Distance of two coordinate points
def distance(lat1, lon1, lat2, lon2):
    r = 6371
    p = pi / 180

    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return (2 * r * asin(sqrt(a)))*1000

# Finds last row in the array
def find_last_row(arr : list):
    last_row = 0
    for i in arr:
        last_row = i.row
    return last_row