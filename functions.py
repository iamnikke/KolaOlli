from queryDb import queryDb
from decimal import Decimal
from geopy import distance
import random

# Get user location
def get_user_location(user_id):

    result = queryDb(f"SELECT location FROM user_info where id = {user_id}")

    return result


# Move player
def move_player(icao, travel_distance, user_money, playerData):

    game_id = playerData.id
    queryDb(f"UPDATE user_info SET location = '{icao}', total_travel_km = '{travel_distance}', money = '{user_money}' WHERE id = '{game_id}'")
    playerData.location = icao

    return True

# Pick transportation method
class Airplane:
    def __init__(self, name, speed, capacity,):
        self.name = name
        self.speed =speed
        self.capacity = capacity

    def __repr__(self):
        return f"Lentokone: (Nimi: {self.name}, Nopeus: {self.speed} km/h, Kapasiteetti: {self.capacity} tölkkiä)"


#tähän voidaan vaihtaa lentokoneiden statseja
def init_vehicles():
    small_airplane = Airplane("pieni lentokone", 1000, 50)
    medium_airplane = Airplane("keskikokoinen lentokone", 1500, 500)
    big_airplane = Airplane("iso lentokone", 2000, 2000)

    # Palautetaan lista kulkuneuvo-olioista
    return [small_airplane, medium_airplane, big_airplane]


# Reduce money
def reduceMoney(playerData, priceAmount):

    # Muuttuja pelkän pelaajan ID:n erottamiseksi oliosta
    playerId = playerData.id

    ## [0][0] = ensimmäinen rivi, ensimmäinen sarake
    moneyBalance = queryDb(f"SELECT money FROM user_info WHERE id = '{playerId}'")[0][0]

    priceAmount = Decimal(str(priceAmount))

    if moneyBalance < priceAmount:
        # debug
        #print("Ei riittävästi rahaa!")
        #print(moneyBalance)

        # Palauta false jos rahat eivät riitä maksuun
        return False

    #print("Rahat riittää")
    #print(moneyBalance)
    newBalance = moneyBalance - priceAmount

    # Päivitä olio
    playerData.money = newBalance
    # Päivitä käyttäjän rahasaldo tietokantaan
    queryDb(f"UPDATE user_info SET money = '{newBalance}' WHERE id = '{playerId}'")

    # Palauta true jos rahat riittävät
    return True


# Effluent
def calculate_effluent(distance):
    effluent = distance*246
    return effluent


# Calculate distance
def calculate_distance(currentLocation, targetCountry):

    # haetaan lentokenttien koordinaatit tietokannasta
    currentLocationXY = queryDb(f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident = '{currentLocation}'")
    targetCountryXY = queryDb(f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident = '{targetCountry}'")

    # laskee lentokenttien etäisyyden
    dist = distance.distance(currentLocationXY, targetCountryXY)
    # print (f"Etäisyys: {dist.km:.2f} km")
    return dist.km


# Calculate fines
def calculate_fines(capacity, load):
    #lasketaan ylilasti
    overload = load - capacity
    #jos ylilastia on enemmän kuin kapasiteettia, törkeä sakko
    if overload > capacity:
        fines = (load - capacity) * 10

        #muuten normisakko
    else:
        fines = (load - capacity) * 5
    # palauta sakon määrä
    return fines


# Calculate fly cost
def calculate_fly_cost(dist):
    price = dist * 0.2
    return price


# Demo function
def demoFunction(currentLocation, targetCountry):

    # Kyselyt tietokantaan (Varmaan väärin mutta tähän tyyliin kuitenkin)
    currentLocationXY = queryDb(f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident = '{currentLocation}'")
    targetCountryXY = queryDb(f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident = '{targetCountry}'")

    print(currentLocationXY)
    print(targetCountryXY)

# KOKEILEMISEKSI KUTSU FUNKTIOTA SAMASSA TIEDOSTOSSA KIINTEILLÄ PARAMETREILLÄ:
demoFunction("EFHK", "EFPE")

# Sen jälkeen valitse pycharm oikealta ylhäältä main -> Current File ja suorita scripti


# Get caught function
def get_caught():
    number = random.randint(0,100)
    if number > 10:
        return True
    else:
        return False

# Lisää rahaa
def add_money(playerData, priceAmount):

    playerId = playerData.id

    ## [0][0] = ensimmäinen rivi, ensimmäinen sarake
    moneyBalance = queryDb(f"SELECT money FROM user_info WHERE id = '{playerId}'")[0][0]

    priceAmount = Decimal(str(priceAmount))

    if moneyBalance < priceAmount:
        # Palauta false jos rahat eivät riitä maksuun
        return False

    newBalance = moneyBalance + priceAmount

    # Päivitä olio
    playerData.money = newBalance
    # Päivitä käyttäjän rahasaldo tietokantaan
    queryDb(f"UPDATE user_info SET money = '{newBalance}' WHERE id = '{playerId}'")

    # Palauta true jos rahat riittävät
    return True

# Päivittää alku ja loppu locationit tietokantaan uusille riveille
def update_passport(currentLocation, targetCountry):

    queryDb(f"INSERT INTO passport(start_location, end_location) VALUES ({currentLocation}, {targetCountry})")

    return True
