class Autocar:
    def __init__(self, weight):
        self.weight = weight

class LightAutocar(Autocar):
    def __init__(self, weight):
        Autocar.__init__(self, weight)

    def allow_parking(self):
        return "ВЕС: %d, ПАРКОВКА РАЗРЕШЕНА" % self.weight

class HeavyAutocar(Autocar):
    def __init__(self, weight):
        Autocar.__init__(self, weight)

    def allow_parking(self):
        return "ВЕС %d, ПАРКОВКА ЗАПРЕЩЕНА" % self.weight

class Parking:
    def __init__(self, place):
        self.place = place

    def amount_place(self):
        return "НА ПАРКОВКЕ %d МЕСТ" % self.place

class KPP:
    __money = 20

    def __init__(self, time):
        self.time = time

    def __price(self):
        return self.time * self.__money

    def get_price(self):
        return "НАДО ЗАПЛАТИТЬ %d РУБЛЕЙ!" % self.__price()

parking = Parking (20)
stop = KPP(4)
lightcar = LightAutocar(12)
heavyautocar = HeavyAutocar(100)

print(parking.amount_place())
print(lightcar.allow_parking())
print(heavyautocar.allow_parking())
print(stop.get_price())
