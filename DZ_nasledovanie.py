
class Car:
    price = 1000000
    def horse_powers(self):
        
        print('У машины 200 л.с.')




class Nissan(Car):

    def __str__(self):
        return f'{self.__class__.__name__}: price = {self.price}'

    def horse_powers(self):
        print(f'У машины {self.__class__.__name__} 160 л.с.')

class Kia(Car):

    def __str__(self):
        return f'{self.__class__.__name__}: price = {self.price}'

    def horse_powers(self):
        print(f'У машины {self.__class__.__name__} 140 л.с.')

nissan = Nissan()
nissan.price = 1500000
print(nissan)
nissan.horse_powers()

kia= Kia()
kia.price = 1300000
print(kia)
kia.horse_powers()