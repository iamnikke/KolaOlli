import mysql.connector

conn = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='cola_game',
    user='',
    password='',
    autocommit=True
)

def move_player(icao, travel_distance, user_money, game_id):
    cursor = conn.cursor(dictionary=True)

    # chekkaa onko icao koodin lentokenttä Euroopassa
    check_sql = f"SELECT continent FROM airport WHERE ident = %s"
    cursor.execute(check_sql, (icao,))
    result = cursor.fetchone()

    # Päivittää arvot tietokantaan, jos icao koodin lentokenttä sijaitsee Euroopassa
    if result and result['continent'] == 'EU':
        sql = 'UPDATE user_info SET location = %s, total_travel_km = %s, money = %s WHERE id = %s'
        cursor.execute(sql, (icao, travel_distance, user_money, game_id))
        conn.commit()
        return True
    else:
        print("Invalid airport: The selected airport is not in Europe or does not exist.")
        return False