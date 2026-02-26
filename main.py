from gameInit import auth



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


auth = auth(username)

userData = f"""
        ID: {auth.id}
        Käyttäjänimi: {auth.username}
        Massit: {auth.money}
        Colat: {auth.coca_cola}
        XP: {auth.xp}
        Kokonaismatkustelu km: {auth.total_travel_km}
        Päästöt: {auth.co2_consumed}
        Nykyinen sijainti: {auth.location}
        Kellonaika: {auth.clock}
        Lahjukset: {auth.bribes}
"""

print(userData)


"""

TESTIT TMS TÄN AlAPUOLELLE
ÄLÄ PUSHAA MITÄÄN PÄÄOHJELMAAN


YLEISPÄTEVÄ OHJE:
jos haluat kokeilla funktiota oikeilla parametreillä, voit käyttää ylläolevan olioluokkaa
datan saamiseksi.

funktiossa voi kuitenkin tarvita muuta, kuten sijainnin koordinaatit, silloin flow ja demo menisi näin:

-> Pääohjelmassa annetaan pelaajan nykysijainti, sekä kohdemaa parametrinä tähän tyyliin:
demoFunction(auth.location, targetCountry)

-> Kokeiluvaiheessa voidaan kovakoodata parametrit funktion sisällä näin:

# importti tietokannan kyselylle koska sitä tarvitaan tässä
import queryDb from queryDb

def demoFunction(currentLocation, targetCountry)
    
    # KOVAKOOdAUKSET TESTIÄ VARTEN
    currentLocation = "EFHK"
    targetCountry = "ABCD"
    
    # Kyselyt tietokantaan (Varmaan väärin mutta tähän tyyliin kuitenkin)
    currentLocationXY = queryDb(f"SELECT longitude, latitude FROM airports WHERE ident = '{currentLocation}')
    targetCountryXY = queryDb(f"SELECT longitude, latitude FROM airports WHERE ident = '{targetCountry}')
    
    ... käsittely jatkuu 

"""
