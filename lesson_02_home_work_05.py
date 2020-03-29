"""
my_list = [7, 5, 3, 3, 2]
print('текущий рейтинг:', my_list)

user_number = int(input('Введите новый элемент рейтинга: '))
if user_number >= 0:
    for el in my_list:
        if user_number > el:
            my_list.insert(my_list.index(el), user_number)
            print('итоговый рейтинг:', my_list)
            break
        elif user_number == el:
            my_list.insert(my_list.index(el) + 1, user_number)
            print('итоговый рейтинг:', my_list)
            break
        elif user_number < my_list[len(my_list) - 1]:
            my_list.append(user_number)
            print('итоговый рейтинг:', my_list)
            break
else:
    print('Введён отрицательный номер')
"""

# разбор задания от преподавателя вариант 1 - плохой (громоздкий)
my_list = [4, 3, 3, 2, 1]

while True:
    print(f'Current rating: {my_list}')
    number = input('Enter rating number or 111 to finish - ')
    if number.lstrip('-').isdigit() and number != '111':
        number = int(number)
        if my_list.count(number):
            my_list.insert(my_list.index(number) + my_list.count(number), number)
        else:
            param = 0
            n_param = 0
            for n, i in enumerate(my_list):
                if number > i:
                    if param < i:
                        param = i
                        n_param = n
                else:
                    n_param = n + 1
            my_list.insert(n_param, number)
    elif not number.isdigit():
        print('Enter number please')
    else:
        break


# разбор задания от преподавателя вариант 2
my_list = [9, 8, 7, 7, 7, 6, 5, 3, 3, 3, 2, 1]
new_number = int(input('Введите новый элемент рейтинга в виде натурального числа: '))
i = 0
for n in my_list:
    if new_number <= n:
        i += 1
my_list.insert(i, new_number)
print(my_list)

# разбор задания от преподавателя вариант 3
my_list = [7, 5, 3, 3, 2]
n = int(input('количество ввода: '))
for it in range(n):
    number = int(input('введите рейтинг'))
    i = 0
    for val in my_list:
        if number > val:
            break
        i += 1
    my_list.insert(i, float(number))
    print(my_list)
