class TooLessEquipment(Exception):
    def __init__(self, text):
        self.text = text


class WareHouse:
    """Для начала на складе:"""
    __off_equip = {
        'printer': 6,
        'xerox': 7,
        'scaner': 3
    }

    def get_total(self):
        """Всего единиц на складе"""
        result = 0
        for value in self.__off_equip:
            result += int((self.__off_equip[value]))
        return result

    def add_item(self):
        """Приход техники на склад"""
        for key in self.__off_equip:
            user_enter = input(f'Вы хотите внести {key}? Если да, нажмите: "Y, если нет - любую клавишу: ')
            if user_enter.upper() == 'Y':
                try:
                    user_quantity = int(input('Сколько штук? '))
                    self.__off_equip[key] += user_quantity
                except ValueError:
                    print('Вы ошиблись с вводом количества')

    def move_item(self):
        """Выдача техники со склада"""
        for key in self.__off_equip:
            user_enter = input(f'Вам нужен {key}? Если да, нажмите: "Y, если нет - любую клавишу: ')
            if user_enter.upper() == 'Y':
                try:
                    user_quantity = int(input('Сколько штук? '))
                    try:
                        if user_quantity > self.__off_equip[key]:
                            raise TooLessEquipment(f'Недостаточно {key} на складе')
                    except TooLessEquipment as err:
                        print(err)
                    else:
                        self.__off_equip[key] -= user_quantity
                except ValueError:
                    print('Вы ошиблись с вводом количества')
            else:
                continue


class OffEquip:
    """Подразделение офисной техники"""
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f'Name: {self.name}, quantity: {self.quantity}'

    def __add__(self, other):
        return self.quantity + other.quantity


class Printer(OffEquip):
    """Отдел принтеров - дочерний от OffEquip"""
    def __init__(self, name, quantity, cartriges):
        super().__init__(name, quantity)
        self.cartriges = cartriges


class Scaner(OffEquip):
    """Отдел сканеров - дочерний от OffEquip"""
    def __init__(self, name, quantity, adapter):
        super().__init__(name, quantity)
        self.adapter = adapter

    @staticmethod
    def hello_from_scaner():
        print('Привет из отдела сканеров')

    def adapt_order(self):
        if self.adapter < 2:
            return 'Закажите на складе запасной адаптер для сканера'


class Xerox(OffEquip):
    """Отдел ксероксов - дочерний от OffEquip"""
    def __init__(self, name, quantity, _toner):
        super().__init__(name, quantity)
        self._toner = _toner

    @property
    def check_toner(self):
        if self._toner < 5:
            return f'Тонера осталось мало, закажите ещё'


w = WareHouse()
print(w._WareHouse__off_equip)
w.add_item()
print(w._WareHouse__off_equip)
w.move_item()
print(w._WareHouse__off_equip)
print(f'Всего техники на складе: {w.get_total()}')

office = OffEquip('printers', 10)
print(office)

printers = Printer('Epson', 10, 25)
print(printers)
print(f'количество картриджей: {printers.cartriges}')

scan = Scaner('Canon', 3, 1)
scan.hello_from_scaner()
print(scan.adapt_order())

xer = Xerox('Xerox', 3, 3)
print(xer.check_toner)
print(f'количество ксероксов и сканеров: {xer + scan}')
