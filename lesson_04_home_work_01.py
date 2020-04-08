from sys import argv
# корректны ли будут закомментированные ниже строки?
# try:
script_name, work_time, hour_cost, bonus = argv
# except ValueError:
#     print('Введите 3 значения')


def salary(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        return a * b + c
    except ValueError:
        print('Данные неверные')


print('Имя скрипта:', script_name)
print('Ваша зарплата', salary(work_time, hour_cost, bonus))
