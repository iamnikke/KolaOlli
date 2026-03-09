from queryDb import *

def addCola(playerData, colaAmount):

    # Muuttuja pelkän pelaajan ID:n erottamiseksi oliosta
    playerId = playerData.id

    ## [0][0] = ensimmäinen rivi, ensimmäinen sarake
    colaBalance = queryDb(f"SELECT coca_cola FROM user_info WHERE id = '{playerId}'")[0][0]

    newBalance = colaBalance + colaAmount

    # Päivitä olio
    playerData.coca_cola = newBalance
    # Päivitä käyttäjän colasaldo tietokantaan
    queryDb(f"UPDATE user_info SET coca_cola = '{newBalance}' WHERE id = '{playerId}'")

    return True