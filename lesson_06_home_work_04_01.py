from random import randint


class Car:
    is_police = True

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

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
        else:
            print('ok')


class PoliceCar(Car):
    def check(self):
        if self.is_police:
            print('Это копы')


car = Car(300, 'red', 'Ока')
print(car.is_police)
car.turn()
car.show_speed()

town = TownCar(90, 'blue', 'Ford')
town.show_speed()

sport = SportCar(300, 'red', 'Ferrari')

work = WorkCar(30, 'green', 'Gaz')
work.show_speed()

pol = PoliceCar(20, 'white', 'Lada')
pol.check()
print(pol.name)
