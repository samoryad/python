""" моё решение (не очень)

my_list_len = int(input('Введите кол-во элементов списка: '))
my_list = []
i = 1
while i <= my_list_len:
    el = input(f'Введите {i} элемент: ')
    my_list.append(el)
    i += 1
print(my_list)

new_list = []
if len(my_list) % 2 == 0:
    while len(my_list) != 0:
        new_list.append(my_list[1])
        new_list.append(my_list[0])
        my_list = my_list[2:]
else:
    while len(my_list) != 1:
        new_list.append(my_list[1])
        new_list.append(my_list[0])
        my_list = my_list[2:]
    new_list.append(my_list[0])

print(new_list)
"""

# разбор задания от преподавателя вариант 1
my_list = list(input('Enter the numbers with out space - '))

for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]

print(my_list)

# вариант 2
a = input('Введите элементы для массива, разделяя их пробелами: ').split()
i = 0
print(f'Оригинальный список {a}')
while i + 1 < len(a):
    if i % 2 == 0:
        a.insert(i, a.pop(i + 1))
    i += 1
print(f'Изменённый список {a}')

# вариант 3
user_list = input('Enter the numbers with space - ').split()
for i in range(1, len(user_list), 2):
    user_list.insert(i - 1, user_list.pop(i))

print(user_list)
