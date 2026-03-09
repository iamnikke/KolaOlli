import random

from gameInit import *
from functions import *
from printWelcomeHud import *

#
# Pääohjelma
#
#

queryDb("SELECT 1")

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

    printSelectCountryHud(playerData)
    targetCountry = input("Syötä maan tunnus: ")

    #tulostaa vaihtoehdot lentokoneille
    vehicles = init_vehicles()

    if targetCountry != "":

        dist = calculate_distance(playerData.location, targetCountry)
        price = float(f"{calculate_fly_cost(dist):.2f}")

        prices = [
            price,
            price * 1.2,
            price * 1.5
        ]

        printSelectAirportHud(vehicles, playerData, prices)

        # käyttäjä valitsee lentokoneen
        try:
            pick_airplane = int(input("\nValitse lentokone (1, 2, 3): ")) - 1
            if 0 <= pick_airplane < len(vehicles):
                selected_vehicle = vehicles[pick_airplane]
                #print(f"Valitsit: {selected_vehicle.name}")
            else:
                print("Virhe! Lentokonetta ei ole olemassa.")
                continue  # menee takaisin main looppiin
        except ValueError:
            print("Anna numero.")
            continue

        price = Decimal(prices[pick_airplane])
        #print(price)

        # input("Paina enter jatkaaksesi...")

        currentco2 = calculate_effluent(dist)
        updatePassport = update_passport(playerData, playerData.location, targetCountry, currentco2)
        updateco2(playerData, currentco2)

        print(f"Lentäminen {targetCountry} maksaa: {price:.2f}")
        print(f"Matkaa on {dist:.0f} kilometriä.")
        print("====================================")

        print("")
        print(f"Sinulla on {playerData.coca_cola} coca-colaa.")
        load =  int(input("Montako tölkkiä colaa otat mukaan myytäväksi? "))

        #input("Paina Enter jatkaaksesi...")

        if reduceMoney(playerData, price) and reduceCola(playerData, load):
            update_time(playerData.id, dist, selected_vehicle.speed)
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
                    if not reduceMoney(playerData, fines):
                        gameover(playerData.id)
                        break
                        # game over-funktio

            # OHJELMA JATKUU
            loadValue = multiply_load(dist, load)
            add_money(playerData, loadValue)
            xpValue = int(dist / 10)
            addXp(playerData, xpValue)

            printWelcomeHud(xpValue, loadValue, playerData)
            #print("Keräsit XP", xpValue)
            #print("Tienasit ", loadValue)
            #print("Rahaa jäljellä", playerData.money)

            # print("DEBUG",playerData.location, "->", playerData.homeport )
            input("Lennä takaisin kotiin painamalla Enter...")
            dist = calculate_distance(playerData.location, playerData.homeport)
            price = float(f"{calculate_fly_cost(dist):.2f}")
            currentco2 = calculate_effluent(dist)
            updatePassportAgain = update_passport(playerData, playerData.location, playerData.homeport, currentco2)
            updateco2(playerData, currentco2)
            update_time(playerData.id, dist, selected_vehicle.speed)
            move_player(playerData.homeport, dist, playerData.money, playerData)

            # Refill inventory -> faija tuo töistä kokista
            colaAmount = random.randint(200,500)
            addCola(playerData, colaAmount)

            if playerData.xp >= 1000:
                printWinner()
                break


            printTripFinished(colaAmount)
            #print("Faija toi sinulle töistä kolaa", colaAmount)


            #printUserStats(playerData.username)

            input("Paina Enter lähteäksesi lentokentälle...")

        else:
            print("Sinut käännytettiin kassalla kotiin. Rahat eivät riittäneet.")
            print("Kokeile lentää lähemmäs. Sinulla on vain", playerData.money)



"""

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
