
class Car:

    price = 1000000
    def __init__(self, power = 200):
        self.power = power
    def horse_powers(self):
        return f'У автомобиля {self.__class__.__name__}, мощность {self.power} л.с.'



class Nissan(Car):

    def __str__(self):
        return f'{self.__class__.__name__}: price = {self.price}'

    def horse_powers(self):
        return f'У автомобиля {self.__class__.__name__}, мощность {self.power - 20} л.с.'
class Kia(Car):

    def __str__(self):
        return f'{self.__class__.__name__}: price = {self.price}'

    def horse_powers(self):
        return f'У автомобиля {self.__class__.__name__}, мощность {self.power - 30} л.с.'

# car = Car()
# car.horse_powers()
# print(car)

nissan = Nissan()
nissan.price = 1500000

print(nissan)
print(nissan.horse_powers())

kia = Kia()
kia.price = 1300000
print(kia)
print(kia.horse_powers())