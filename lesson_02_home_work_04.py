user_str = input('Введите строку через пробел: ')

user_str = list(user_str.split(' '))
for i, n in enumerate(user_str):
    if len(n) < 10:
        print(i + 1, n)
    else:
        print(i + 1, n[:10])


# разбор задания от преподавателя вариант 1
string = (input('Enter the numbers with space - ')).split()
print(string)

for i in range(len(string)):
    if len(string[i]) <= 10:
        print(i, string[i])
    else:
        print(i, (string[i])[:10])

# разбор задания от преподавателя вариант 2 - тернарный оператор
string = (input('Enter the numbers with space - ')).split()
print(string)

for n, i in enumerate(string):
    print(n + 1, i) if len(i) <= 10 else print(n, (i[:10]))

# разбор задания от преподавателя вариант 3 - оптимальный
my_string = (input('Введите строку из нескольких слов, разделённых пробелами: ')).split()
print(string)
for i, word in enumerate(my_string, 1):
    print(f'{i} {word[:10]}')