def printWelcomeHud(xpValue, loadValue, playerData):
    print("""
    ========================================





          ////^\\\\
          | ^   ^ |
         @ (o) (o) @
          |   <   |
          |  ___  |
           \\_____/
         ____|  |____
    ========================
    > Saavuit kohteeseen.

    Tervetuloa maahan!
    """)

    print(f"Ansaitsit {xpValue} tasopistettä!")
    print(f"Sinulla on nyt yhteensä {playerData.xp:.2f} tasopistettä!")
    print("")
    print(f"Tienasit {loadValue:.2f} €!")
    print(f"Sinulla on nyt {playerData.money:.2f} €!")


def printTripFinished(colaAmount):
    print("========================================")
    print("""

                 ,#####,
                 #_   _#
                 |a` `a|
                 |  u  |
                 \\  =  /
                 |\\___/|
        ___ ____/:     :\\____ ___
      .'   `.-===-\\   /-===-.`   '.
     /      .-\"\"\"\"\"--\"\"\"\"\"-.      \\\\              ////^\\\\
    /'             =:=             '\\\\            | ^   ^ |
  .'  ' .:    o   -=:=-   o    :. '  `.          @ (o) (o) @
  (.'   /'. '-.....-|-.....-' .'\\   '.)           |   <   |
  /' ._/   ".     --:--     ."   \\_. '\\\\          |  ___  |
 |  .'|      ".  ---:---  ."      |'.  |           \\_____/
 |  : |       |  ---:---  |       | :  |         ____|  |____
    ========================
    > Saavuit kotiin.
          """)
    print(f"Faija toi sinulle töistä {colaAmount} colaa.")


def printWinner():
    print("========================================")
    print("""

                     ,#####,
                     #_   _#
                     |a` `a|
                     |  u  |
                     \\  =  /
                     |\\___/|
            ___ ____/:     :\\____ ___
          .'   `.-===-\\   /-===-.`   '.
         /      .-\"\"\"\"\"--\"\"\"\"\"-.      \\\\              ////^\\\\
        /'             =:=             '\\\\            | ^   ^ |
      .'  ' .:    o   -=:=-   o    :. '  `.          @ (o) (o) @
      (.'   /'. '-.....-|-.....-' .'\\   '.)           |   <   |
      /' ._/   ".     --:--     ."   \\_. '\\\\          |  ___  |
     |  .'|      ".  ---:---  ."      |'.  |           \\_____/
     |  : |       |  ---:---  |       | :  |         ____|  |____
        ========================
        > Voitit pelin. Faija on ylpiä!
              """)