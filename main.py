from calculate_distance import calculate_distance
from calculate_fly_cost import calculate_fly_cost
from move_player import move_player
from reduceMoney import reduceMoney
from gameInit import *
from get_caught import get_caught
from calculate_fines import calculate_fines

#
# Pääohjelma
#
#

# Alkutekstit
## r-string estää tulkitsemasta erikoismerkkejä
print(r"""
      ////^\\\\
      | ^   ^ |
     @ (o) (o) @
      |   <   |
      |  ___  |
       \_____/
     ____|  |____
========================
 _  __     _        ___  _ _ _ 
| |/ /___ | | __ _ / _ \| | (_)
| ' // _ \| |/ _` | | | | | | |
| . \ (_) | | (_| | |_| | | | |
|_|\_\___/|_|\__,_|\___/|_|_|_|
""")
username = input("Anna pelaajan nimimerkki: ")
print("===================")

# Pelin alustus ja olioluokan luonti.
playerData = auth(username)

# Tulosta pelaajan statsit
printUserStats(playerData.username)

while True:
    targetCountry = input("Syötä maan tunnus: ")

    if targetCountry != "":
        dist = calculate_distance(playerData.location, targetCountry)
        price = float(f"{calculate_fly_cost(dist):.2f}")

        print(f"Lentäminen {targetCountry} maksaa: {price}")
        print(f"Matkaa on {dist:.2f} kilometriä.")
        print("====================================")

        confirm = input("Kirjoita lessgo matkustaaksesi: ")
        if confirm == "lessgo":
            if reduceMoney(playerData, price):
                print("Tervetuloa maahan.")
                print("Rahaa jäljellä", playerData.money)
                move_player(targetCountry, dist, playerData.money, playerData)
                if get_caught():
                    fines = calculate_fines(100, 110)
                    print(f"Jäit kiinni ylilastin kanssa, joudut maksamaan sakon: {fines} euroa")
                    if reduceMoney(playerData, fines):
                        print("Rahaa jäljellä", playerData.money)


                printUserStats(playerData.username)

            else:
                print("Sinut käännytettiin kassalla kotiin. Rahat eivät riittäneet.")
                print("Kokeile lentää lähemmäs. Sinulla on vain", playerData.money)



"""

TESTIT TMS TÄN AlAPUOLELLE
ÄLÄ PUSHAA MITÄÄN PÄÄOHJELMAAN


YLEISPÄTEVÄ OHJE:
jos haluat kokeilla funktiota oikeilla parametreillä, voit käyttää ylläolevan olioluokkaa
datan saamiseksi.

funktiossa voi kuitenkin tarvita muuta, kuten sijainnin koordinaatit, silloin flow ja demo menisi näin:

-> Pääohjelmassa annetaan pelaajan nykysijainti, sekä kohdemaa parametrinä tähän tyyliin:
demoFunction(auth.location, targetCountry)

-> Kokeiluvaiheessa voidaan kutsua sitä kovakoodatuilla parametreillä funktion sisällä näin:

# importti tietokannan kyselylle koska sitä tarvitaan tässä
from queryDb import queryDb

def demoFunction(currentLocation, targetCountry):

    # Kyselyt tietokantaan
    currentLocationXY = queryDb(f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident = '{currentLocation}'")
    targetCountryXY = queryDb(f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident = '{targetCountry}'")

    print(currentLocationXY)
    print(targetCountryXY)

# KOKEILEMISEKSI KUTSU FUNKTIOTA SAMASSA TIEDOSTOSSA KIINTEILLÄ PARAMETREILLÄ:
demoFunction("EFHK", "EFPE")

# Sen jälkeen valitse pycharm oikealta ylhäältä main -> Current File ja suorita scripti  

"""