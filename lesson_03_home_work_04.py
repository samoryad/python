def my_func_01(x, y):
    x = x ** y
    return x


def my_func_02(x, y):
    z = 1
    for y in range(0, y, -1):
        z = z * x
    x = 1 / z
    return x


print(round(my_func_01(36, -2), 10))
print(round(my_func_02(36, -2), 10))


# Решение от преподавателя №1
def my_pow_fun(x, y):
    try:
        res = x ** y
    except TypeError:
        return 'Enter a float number and a negative power'
    return res


print(my_pow_fun(36, -2))


# Решение от преподавателя №2
def power(x, y):
    try:
        x, y = float(x), int(y)
        res = x
        for _ in range(abs(y)-1):
            res *= x
        return f'{1/res:.4f}'
    except ValueError:
        return 'Value error'


print(power(input('Первое значение - '), input('Второе значение - ')))
