from functions import *

def printSelectAirportHud(vehicles, playerData, prices):

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
          Ja {playerData.money} euroa rahaa
    """)

    i = 0

    for vehicle in vehicles:
        i += 1

        print(f"""
        {i}. {vehicle.name} 
        Nopeus: {vehicle.speed} km/h 
        Kapasiteetti: {vehicle.capacity} tölkkiä
        Hinta: {prices[i-1]:.2f} €
        """)

    print("========================================")