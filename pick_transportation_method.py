class Airplane:
    def __init__(self, name, speed, capacity,):
        self.name = name
        self.speed =speed
        self.capacity = capacity

    def __repr__(self):
        return f"Lentokone: (Nimi: {self.name}, Nopeus: {self.speed} km/h, Kapasiteetti: {self.capacity} tölkkiä)"


#tähän voidaan vaihtaa lentokoneiden statseja
def init_vehicles():
    small_airplane = Airplane("pieni lentokone", 1000, 50)
    medium_airplane = Airplane("keskikokoinen lentokone", 1500, 500)
    big_airplane = Airplane("iso lentokone", 2000, 2000)

    # Palautetaan lista kulkuneuvo-olioista
    return [small_airplane, medium_airplane, big_airplane]