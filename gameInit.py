from queryDb import queryDb
from instructions import printInstructions

class User:
    def __init__(self, id, username, money, coca_cola, xp, total_travel_km, total_co2_consumed, location, clock, bribes, bribes_succeeded, caught, sales):
        self.id = id
        self.username = username
        self.money = money
        self.coca_cola = coca_cola
        self.xp = xp
        self.total_travel_km = total_travel_km
        self.total_co2_consumed = total_co2_consumed
        self.location = location
        self.clock = clock
        self.bribes = bribes
        self.bribes_succeeded = bribes_succeeded
        self.caught = caught
        self.sales = sales



# Autentikointi funktio, käyttäjän syöttämä nimimerkki parametrinä
def auth(username):

    # Uuden pelaajan oletusasetukset
    defaultUsername = "Matti Oletus"
    defaultBalance = 1000
    defaultCocaCola = 100
    defaultXp = 0
    defaultTotalTravelKm = 0
    defaultTotalCo2Consumed = 0
    defaultLocation = 'EFHK'
    defaultClock = '16:00:00'
    defaultBribes = 0
    defaultBribes_succeeded = 0
    defaultCaught = 0
    defaultsales = 0

    # createUser funktio auth() sisällä jotta se saa oletusarvot
    def createUser(newUsername):
        queryDb(f"""
        INSERT INTO user_info (
            username, 
            money, 
            coca_cola, 
            xp, 
            total_travel_km,
            total_co2_consumed, 
            location, 
            clock, 
            bribes,
            bribes_succeeded,
            caught,
            sales
        ) VALUES (
            '{newUsername}', 
            {defaultBalance}, 
            {defaultCocaCola}, 
            {defaultXp},
            {defaultTotalTravelKm}, 
            {defaultTotalCo2Consumed},
            '{defaultLocation}', 
            '{defaultClock}', 
            {defaultBribes},
            {defaultBribes_succeeded},
            {defaultCaught},
            {defaultsales}
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
            total_co2_consumed=validateUserResult[6],
            location=validateUserResult[7],
            clock=validateUserResult[8],
            bribes=validateUserResult[9],
            bribes_succeeded=validateUserResult[10],
            caught=validateUserResult[11],
            sales=validateUserResult[12]
        )

        #print("DEBUG: gameInit = Käyttäjä löytyi -> Olio-luokan luonti onnistui. Palautetaan pääohjelmaan")
        return user

    # Käyttäjää ei löydy
    else:

        print("Luodaan uusi pelaaja...")

        # Fallback default käyttäjänimeen jos syöte oli tyhjä
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
                total_co2_consumed=validateUserResult[6],
                location=validateUserResult[7],
                clock=validateUserResult[8],
                bribes=validateUserResult[9],
                bribes_succeeded=validateUserResult[10],
                caught=validateUserResult[11],
                sales=validateUserResult[12]
            )
            print("Tervetuloa!")
            printInstructions()
            return user