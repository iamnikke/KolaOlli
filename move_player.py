from queryDb import queryDb

def move_player(icao, travel_distance, user_money, playerData):

    game_id = playerData.id

    queryDb(f"UPDATE user_info SET location = '{icao}', total_travel_km = '{travel_distance}', money = '{user_money}' WHERE id = '{game_id}'")
    playerData.location = icao
    return True