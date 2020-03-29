month = int(input('Введите месяц от 1 до 12: '))

winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
if month in winter:
    print('Это зима')
elif month in spring:
    print('Это весна')
elif month in summer:
    print('Это лето')
elif month in autumn:
    print('Это осень')

my_dict = {1: 'Это зима', 2: 'Это зима', 3: 'Это весна', 4: 'Это весна', 5: 'Это весна', 6: 'Это лето', 7: 'Это лето',
        8: 'Это лето', 9: 'Это осень', 10: 'Это осень', 11: 'Это осень', 12: 'Это зима'}
if month in my_dict:
    print(my_dict.get(month))


# разбор задания от преподавателя вариант 1
month = int(input('Введите интересующий Вас месяц года от 1 до 12:'))

month_dict = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь', 7: 'июль', 8: 'август',
              9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}

month_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь',
              'ноябрь', 'декабрь']
for key in month_dict:
    if key == month:
        print(f'{month}-й месяц года - {month_dict[key]}')
        print(f'{month}-й месяц года - {month_list[month - 1]}')

print(f'Вы ввели некорректный месяц - {month}')


# разбор задания от преподавателя вариант 2
month = int(input('Введите номер месяца:'))
while month < 0 or month > 12:
    month = int(input('Неверно, введите номер месяца: '))

seasons = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer', 8: 'summer',
           9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}
print(seasons[month])

# разбор задания от преподавателя вариант 3
month = int(input('Введите номер месяца:'))
while month < 0 or month > 12:
    month = int(input('Неверно, введите номер месяца: '))

seasons = ('winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer',
           'autumn', 'autumn', 'autumn', 'winter')
print(seasons[month - 1])


