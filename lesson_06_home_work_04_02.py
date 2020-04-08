from random import randint

class Car:
    speed = int(input('Введите скорость: '))
    color = 'blue'
    name = 'BMW'
    is_police = True

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self):
        my_list = ['налево', 'направо']
        print(f'Машина повернула {my_list[randint(0, 1)]}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Скорость превышена')

class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Скорость превышена')


class PoliceCar(Car):
    def check(self):
        if self.is_police:
            print('Это копы')


car = Car()
print(car.name)
car.show_speed()
car.turn()

town = TownCar()
town.show_speed()

sport = SportCar()

work = WorkCar()
work.show_speed()

pol = PoliceCar()
pol.check()