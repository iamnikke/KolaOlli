from queryDb import queryDb

def reduceMoney(playerData, priceAmount):

    # Muuttuja pelkän pelaajan ID:n erottamiseksi oliosta
    playerId = playerData.id

    ## [0][0] = ensimmäinen rivi, ensimmäinen sarake
    moneyBalance = queryDb(f"SELECT money FROM user_info WHERE id = '{playerId}'")[0][0]

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