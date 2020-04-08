import time


def out_red(text):
    print("\033[31m\033[41m {}" .format(text))


def out_yellow(text):
    print("\033[33m\033[43m {}" .format(text))


def out_green(text):
    print("\033[32m\033[42m {}".format(text))


class TrafficLight:
    __color = {}

    def running(self):
        for a in range(1, 4):
            b = input(f'Введите цвет № {a} светофора по порядку (к, ж, з): ')
            self.__color.update({a: b.lower()})
        self.__color.update({4: 'ж'})
        if self.__color == {1: 'к', 2: 'ж', 3: 'з', 4: 'ж'}:
            while True:
                for key in self.__color:
                    if key == 1:
                        out_red(self.__color[key])
                        time.sleep(7)
                    elif key == 3:
                        out_green(self.__color[key])
                        time.sleep(7)
                    else:
                        out_yellow(self.__color[key])
                        time.sleep(2)
        else:
            print('Данные введены неверно')


traf = TrafficLight()
print(traf.running())
