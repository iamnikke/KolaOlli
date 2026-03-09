from functions import *

def printSelectAirportHud(vehicles, playerData):

    print("========================================")

    print(f"""
           _
         -=\\`\\
     |\\ ____\\_\\__
   -=\\c`"*"*"*"* "`)
      `~~~~~/ /~~`
        -==/ /
          '-'
          
          VALITSE LENTOKONE
          Sinulla on {playerData.coca_cola} colaa
    """)

    i = 0

    for vehicle in vehicles:

        print(f"""
        {i + 1}. {vehicle.name} 
        Nopeus: {vehicle.speed} km/h 
        Kapasiteetti: {vehicle.capacity} tölkkiä
        """)

    print("========================================")