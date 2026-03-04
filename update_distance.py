#kasvatetaan kokonaismatkaa
from queryDb import queryDb


def updatedistance(playerData, amount):
    playerId = playerData.id
    currentDistanceAmount = queryDb(f"select total_travel_km from user_info where id = '{playerId}'")[0][0]
    newDistanceAmount = currentDistanceAmount + amount

    playerData.total_travel_km = newDistanceAmount
    queryDb(f"UPDATE user_info SET total_travel_km='{newDistanceAmount}' WHERE id = '{playerId}'")
    return True
