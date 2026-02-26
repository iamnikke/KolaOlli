import mysql.connector

conn = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='cola_game',
    user='',
    password='',
    autocommit=True
)

def get_user_location(user_id):
    cursor = conn.cursor(dictionary=True)

    sql = f"SELECT location FROM user_info where id = %s"
    cursor.execute(sql, (user_id,))
    result = cursor.fetchone()

    return result