from geopy import distance
from queryDb import queryDb

def calculate_distance(currentLocation, targetCountry):

    #
    currentLocationXY = queryDb(f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident = '{currentLocation}'")
    targetCountryXY = queryDb(f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident = '{targetCountry}'")

    dist = distance.distance(currentLocationXY, targetCountryXY)

    return dist




