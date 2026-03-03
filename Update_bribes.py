
from queryDb import queryDb


def updatebribes(playerData,amount):
    playerId = playerData.id
    currentBribesAmount = queryDb(f"select bribes from user_info where id = '{playerId}'")[0][0]
    newBribesAmount = currentBribesAmount + amount

    playerData.bribes = newBribesAmount
    queryDb(f"UPDATE user_info SET bribes='{newBribesAmount}' WHERE id = '{playerId}'")
    return True

