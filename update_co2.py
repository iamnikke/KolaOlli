# päästöt
from queryDb import queryDb


def updateco2(playerData, amount):
    playerId = playerData.id
    currentCo2Consumed = queryDb(f"select total_co2_consumed from user_info where id = '{playerId}'")[0][0]
    newCo2Consumed = currentCo2Consumed + amount

    playerData.total_co2_consumed = newCo2Consumed
    queryDb(f"UPDATE user_info SET total_co2_consumed='{newCo2Consumed}' WHERE id = '{playerId}'")
    return True
