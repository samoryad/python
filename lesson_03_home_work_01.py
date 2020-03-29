def my_f(a, b):
    """Функция проверяет деление на 0 и выводит частное от двух чисел, округлённое до 10 знаков"""
    try:
        return round(a / b, 10)
    except ZeroDivisionError:
        print('Делить на 0 нельзя!')


while True:
    try:
        first = float(input('Введите первое число: '))
        second = float(input('Введите второе число: '))
        break
    except ValueError or TypeError:
        print("Пожалуйста введите число")
print(my_f(first, second))


# Решение от преподавателя
def div(s_1, s_2):
    try:
        s_1, s_2 = int(s_1), int(s_2)
        div_num = s_1/s_2
    except ValueError:
        return "Value error"
    except ZeroDivisionError:
        return "Division by zero forbidden!!!"
    return div_num


print(div(input('Enter first number - '), input('Enter second - ')))

