from queryDb import *

#lisää xptä

def addXp(playerData, xpAmount):

    # Muuttuja pelkän pelaajan ID:n erottamiseksi oliosta
    playerId = playerData.id

    ## [0][0] = ensimmäinen rivi, ensimmäinen sarake
    xpBalance = queryDb(f"SELECT xp FROM user_info WHERE id = '{playerId}'")[0][0]

    newBalance = xpBalance + xpAmount

    # Päivitä olio
    playerData.xp = newBalance
    # Päivitä käyttäjän xp tietokantaan
    queryDb(f"UPDATE user_info SET xp = '{newBalance}' WHERE id = '{playerId}'")

    return True