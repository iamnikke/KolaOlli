import mysql.connector
import os


#AJAMALLA SKRIPTIN SAAT TIETOKANNAN OMALLE TIETOKONEESI MARIADB:LLE
# Täytä tietosi kohtiin jossa lukee täytä

DB_CONFIG = {
    'user': 'täytä',
    'password': 'täytä',
    'host': 'täytä',
    'autocommit': True
}
DB_NAME = 'täytä'
SQL_FILE = 'db.sql'


def setup_database():
    conn = None
    cursor = None

    try:
        # Ottaa yhteyden mariadb ja tekee tietokannan.
        # (**DB_CONFIG) ottaa arvot ylempää avainsanoiksi ja passaa ne connector.connect
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        cursor.execute(f"USE {DB_NAME}")

        # Lukee sql tiedoston, jos löytää. Error viesti, jos ei
        if not os.path.exists(SQL_FILE):
            raise FileNotFoundError(f"Tiedosto '{SQL_FILE}' ei löytynyt.")

        with open(SQL_FILE, 'r', encoding='utf-8') as f:
            # Splitataan sql filen funktiot puolipilkulla, jotta ne voidaan ajaa yksi kerrallaan.
            # Tämä tekee tietokannan tekemisestä sujuvampaa
            sql_statements = f.read().split(';')

        # Executee sql filen. strip() poistaa turhat välilyönnit
        for statement in sql_statements:
            clean_statement = statement.strip()
            if clean_statement:
                cursor.execute(clean_statement)

        print(f"Tietokanta '{DB_NAME}' tiedostosta {SQL_FILE} ollaan luotu onnistuneesti.")

    except Exception as e:
        # Simplified to one clear error message
        print(f"Error: Tietokannan luominen epäonnistui: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()


setup_database()