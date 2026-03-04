from gameInit import *
from functions import *

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

    #tulostaa vaihtoehdot lentokoneille
    vehicles = init_vehicles()

    print("\nValitse lentokoneesi:")
    for i, v in enumerate(vehicles):
        print(f"{i + 1}. {v.name} (Nopeus: {v.speed} km/h, Kapasiteetti: {v.capacity} tölkkiä)")

    #käyttäjä valitsee lentokoneen
    try:
        pick_airplane = int(input("\nValitse lentokone (1, 2, 3): ")) - 1
        if 0 <= pick_airplane < len(vehicles):
            selected_vehicle = vehicles[pick_airplane]
            print(f"Valitsit: {selected_vehicle.name}")
        else:
            print("Virhe! Lentokonetta ei ole olemassa.")
            continue  # menee takaisin main looppiin
    except ValueError:
        print("Anna numero.")
        continue

    if targetCountry != "":
        dist = calculate_distance(playerData.location, targetCountry)
        price = float(f"{calculate_fly_cost(dist):.2f}")
        currentco2 = calculate_effluent(dist)
        updatePassport = update_passport(playerData.id, playerData.location, targetCountry, currentco2)

        print(f"Lentäminen {targetCountry} maksaa: {price}")
        print(f"Matkaa on {dist:.2f} kilometriä.")
        print("====================================")

        load =  int(input("Kuinka monta tölkkiä colaa otat mukaan?"))

        confirm = input("Kirjoita lessgo matkustaaksesi: ")
        if confirm == "lessgo":
            if reduceMoney(playerData, price) and reduceCola(playerData, load):
                print("Tervetuloa maahan.")
                update_time(playerData.id, dist, selected_vehicle.speed)
                print("Rahaa jäljellä", playerData.money)
                move_player(targetCountry, dist, playerData.money, playerData)
                capacity = selected_vehicle.capacity

                if capacity < load:
                    # Arpoo jääkö pelaaja kiinni tullissa
                    if get_caught():
                        # laskee sakon
                        fines = calculate_fines(capacity, load)
                        print(f"Jäit kiinni ylilastin kanssa, joudut maksamaan sakon: {fines} euroa")

                        # attempt bribe
                        bribe = input("Lahjonta: yes / no: ")
                        bribePrice = fines * 0.2
                        print("Lahjonta maksaa", bribePrice)

                        if bribe == "yes":
                            # Yritä lahjoa -> vähennä lahjonnan hinta
                            if reduceMoney(playerData, bribePrice):
                                # Arvo suostuuko tullivirkailija lahjukseen, jos ei, eli jää kiinni niin sakko x 2
                                if get_caught():
                                    fines = fines * 2
                                # Jos suostuu niin sakot nolla
                                else:
                                    fines = 0
                            # Else jos rahat ei riitä lahjukseen
                            else:
                                print("Rahat ei riitä lahjontaan")

                        # Jos rahat riittää maksuun
                        if reduceMoney(playerData, fines):
                            print("Rahaa jäljellä", playerData.money)
                        # rahat ei riitä sakkoon
                        else:
                            print("Game over tulossa pian")
                            break
                            # game over-funktio
                else:
                    loadValue = multiply_load(dist, load)
                    add_money(playerData, loadValue)
                    print("Selvisit tullista")


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
