from functions import *

def printSelectCountryHud(playerData):

    allowedCountries = {
        'Austria': 'LOWW',
        'Bryssel, Belgium': 'EBBR',
        'Madrid, Espanja': 'LEMD',
        'Rooma, Italia': 'LIRF',
        'Luxemburg, Luxemburg': 'ELLX',
        'Varsova, Puola': 'EPWA',
        'Pariisi, Ranska': 'LFPG',
        'Kööpenhamina, Tanska': 'EKCH',
        'Ankara, Turkki': 'LTAC',
        'Minsk, Valko-Venäjä': 'UMMS',
        'Viro, Tallinna': 'EETN',
    }

    print("========================================")

    for country, icao in allowedCountries.items():
        dist = calculate_distance(playerData.location, icao)
        price = float(f"{calculate_fly_cost(dist):.2f}")

        canAfford = ""

        if playerData.money > price:
            canAfford = "Rahat riittää ✅"
        else:
            canAfford = "Rahat eivät riitä ❌"

        print(icao + " --> " + country)
        print("     ", int(dist), "km päässä | Meno-paluu", price, "€ | ", canAfford)
        print("")


    print("========================================")