from queryDb import queryDb
# Reduce cola
def reduceCola(playerData, colaAmount):

    # Muuttuja pelkän pelaajan ID:n erottamiseksi oliosta
    playerId = playerData.id

    ## [0][0] = ensimmäinen rivi, ensimmäinen sarake
    colaBalance = queryDb(f"SELECT coca_cola FROM user_info WHERE id = '{playerId}'")[0][0]



    if colaBalance < colaAmount:
        # debug
        #print("Ei riittävästi colaa!")
        #print(colaBalance)

        # Palauta false jos colaa ei tarpeeksi stashis
        return False


    newBalance = colaBalance - colaAmount

    # Päivitä olio
    playerData.coca_cola = newBalance
    # Päivitä käyttäjän colasaldo tietokantaan
    queryDb(f"UPDATE user_info SET coca_cola = '{newBalance}' WHERE id = '{playerId}'")

    # Palauta true jos colaa tarpeeks
    return True