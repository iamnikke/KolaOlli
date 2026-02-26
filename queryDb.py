import mysql.connector

def queryDb(query):

    mysql_connection = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        password="Aaro22",
        database="cola_game",
        autocommit=True
    )
    cursor = mysql_connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    mysql_connection.close()
    return result