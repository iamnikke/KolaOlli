import random

from queryDb import queryDb

class User:
    def __init__(self, id, username, money, coca_cola, xp, total_travel_km, co2_consumed, location, clock, bribes):
        self.id = id
        self.username = username
        self.money = money
        self.coca_cola = coca_cola
        self.xp = xp
        self.total_travel_km = total_travel_km
        self.co2_consumed = co2_consumed
        self.location = location
        self.clock = clock
        self.bribes = bribes


# Autentikointi funktio, käyttäjän syöttämä nimimerkki parametrinä
def auth(username):

    # Uuden pelaajan oletusasetukset
    defaultId = random.randint(1,999) # TILAPÄINEN RATKAISU ID:LLE, KORVATAAN AUTO INCREMENT
    defaultUsername = "Matti Oletus"
    defaultBalance = 0
    defaultCocaCola = 0
    defaultXp = 0
    defaultTotalTravelKm = 0
    defaultCo2Consumed = 0
    defaultLocation = 'EFHK'
    defaultClock = '16:00:00'
    defaultBribes = 0

    # Siirretään createUser tänne, jotta se näkee oletusarvot
    def createUser(new_username):
        queryDb(f"""
        INSERT INTO user_info (
            id,
            username, 
            money, 
            coca_cola, 
            xp, 
            total_travel_km,
            co2_consumed, 
            location, 
            clock, 
            bribes
        ) VALUES (
            {defaultId},
            '{new_username}', 
            {defaultBalance}, 
            {defaultCocaCola}, 
            {defaultXp},
            {defaultTotalTravelKm}, 
            {defaultCo2Consumed},
            '{defaultLocation}', 
            '{defaultClock}', 
            {defaultBribes}
        )
        """)


    validateUser = queryDb(f"SELECT * FROM user_info WHERE username = '{username}'")

    # Jos query palauttaa tuloksen, käyttäjä löytyy tietokannasta
    if validateUser:

        # Käsitellään vain ensimmäistä riviä
        validateUserResult = validateUser[0]

        user = User(
            id=validateUserResult[0],
            username=validateUserResult[1],
            money=validateUserResult[2],
            coca_cola=validateUserResult[3],
            xp=validateUserResult[4],
            total_travel_km=validateUserResult[5],
            co2_consumed=validateUserResult[6],
            location=validateUserResult[7],
            clock=validateUserResult[8],
            bribes=validateUserResult[9]
        )

        print("DEBUG: gameInit = Käyttäjä löytyi -> Olio-luokan luonti onnistui. Palautetaan pääohjelmaan")
        return user

    # Käyttäjää ei löydy
    else:

        print("\nKäyttäjää ei löydy. Tehdään sinulle uusi!")
        username = input("Syötä käyttäjänimi: ").strip()

        if username == "":
            username = defaultUsername

        createUser(username)

        # Hae juuri luotu käyttäjä
        validateUser = queryDb(f"SELECT * FROM user_info WHERE username = '{username}'")
        if validateUser:
            validateUserResult = validateUser[0]
            user = User(
                id=validateUserResult[0],
                username=validateUserResult[1],
                money=validateUserResult[2],
                coca_cola=validateUserResult[3],
                xp=validateUserResult[4],
                total_travel_km=validateUserResult[5],
                co2_consumed=validateUserResult[6],
                location=validateUserResult[7],
                clock=validateUserResult[8],
                bribes=validateUserResult[9]
            )
            print("Onnistui")
            return user