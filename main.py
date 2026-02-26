from gameInit import auth
from reduceMoney import reduceMoney


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
playerStatsHud = f"""
        ID: {playerData.id}
        Käyttäjänimi: {playerData.username}
        Massit: {playerData.money}
        Colat: {playerData.coca_cola}
        XP: {playerData.xp}
        Kokonaismatkustelu km: {playerData.total_travel_km}
        Päästöt: {playerData.co2_consumed}
        Nykyinen sijainti: {playerData.location}
        Kellonaika: {playerData.clock}
        Lahjukset: {playerData.bribes}
"""
print(playerStatsHud)

# Funktion testaus
if reduceMoney(playerData,20):
    print("Rahat riitti")
    print("Uusi saldo", playerData.money)
else:
    print("Rahat ei riittänyt")
    print(playerData.money)


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