
class Car:
    price = 1000000
    def horse_powers(self, power):
        self.pw = power



class Nissan(Car):

    def __str__(self):
        return f'{self.__class__.__name__}: price = {self.price}, horse power = {self.pw}'
class Kia(Car):

    def __str__(self):
        return f'{self.__class__.__name__}: price = {self.price}, horse power = {self.pw}'

nissan = Nissan()
nissan.price = 1500000
nissan.horse_powers(186)
print(nissan)

kia= Kia()
kia.price = 1300000
kia.horse_powers(155)
print(kia)