from geopy import distance
from queryDb import queryDb

def calculate_distance(currentLocation, targetCountry):

    # haetaan lentokenttien koordinaatit tietokannasta
    currentLocationXY = queryDb(f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident = '{currentLocation}'")
    targetCountryXY = queryDb(f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident = '{targetCountry}'")

    # laskee lentokenttien etäisyyden
    dist = distance.distance(currentLocationXY, targetCountryXY)
    print (f"Etäisyys: {dist.km:.2f} km")
    return dist.km

dista = calculate_distance('agar','efhk')
calculate_fly_cost(dista)




