from gameInit import auth



#
# Pääohjelma
#
#

# Alkutekstit
print("===================")
print("")
print("Tervetuloa")
print("Kirjaudu sisään")
print("===================")

username = input("Käyttäjänimi")
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

riitaako(auth.id)