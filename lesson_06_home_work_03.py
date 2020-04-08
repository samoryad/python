# решение без конструктора
class Worker:
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    position = input('Введите должность: ')
    _income = {'salary': int(input('Введите зарплату: ')), 'bonus': int(input('Введите премию: '))}


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        total = 0
        for el in self._income.values():
            total += el
        return total


job = Position()
print(f'Должность: {job.position}')
print(f'Словарь: {job._income}')
print(f'Сотрудник: {job.get_full_name()} ')
print(f'Зарплата с премией: {job.get_total_income()} ')


"""
# решение через конструктор
class Worker:
    def __init__(self, name, surname, position, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'salary': salary, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        total = 0
        for el in self._income.values():
            total += el
        return total


job = Position('Вася', 'Пупкин', 'Директор', 50000, 10000)
print(f'Сотрудник: {job.get_full_name()} ')
print(f'Зарплата: {job.get_total_income()} ')
"""