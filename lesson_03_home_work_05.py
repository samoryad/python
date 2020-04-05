"""

total = 0
while True:
    my_str = input('Введите несколько чисел через пробел и нажмите "enter". Для выхода нажмите "Q".\n - ').split()
    if my_str.count('Q') or my_str.count('q') == 0:
        for el in my_str:
            total += float(el)
        print('сумма', total)
    elif my_str.count('Q') or my_str.count('q') == 1:
        my_str = my_str[:(len(my_str) - 1)]
        for el in my_str:
            total += float(el)
        print('итого:', total)
        break


# Решение от преподавателя №1
def summary():
    ex = False
    fResult = 0
    while ex == False:
        lNumbers = input('Input numbers divided by whitespaces or q to quit: ').split()
        result = 0
        for i in range(len(lNumbers)):
            if lNumbers[i] == 'q':
                ex = True
                break
            else:
                result = result + int(lNumbers[i])
            fResult = fResult + result
        print(f'Current sum is {fResult}')
    print(f"You've quited! Final sum is {fResult}")


summary()


# Решение от преподавателя №2
def summary():
    result = 0
    while True:
        print(f'Текущая сумма = {result}')
        input_s = input('Введите строку чисел, разделённых пробелом ' \
                        'для подсчёта суммы (# - символ для завершения): \n').split()
        for value in input_s:
            if value == '#':
                print(f'Окончательная сумма = {result}')
                break
            try:
                result += float(value)
            except ValueError:
                print(f'Значение {value} не было учтено при подсчёте суммы - неверный тип')
        else:
            # если символа завершения программы введено не было, то продолжаем ввод данных
            continue
        # сюда мы дойдём только, если встретим символ завершения программы
        break
    return f'Окончательная сумма = {result}'


summary()
"""

# Решение от преподавателя №3 Только ядро, можно доделать
num = 0
try:
    while num != '#':
        for i in map(int, input('Для выхода наберите "#" \nВведите числа, используя пробел. \n').split()):
            num += i
        print(num)
except ValueError:
    print(num)