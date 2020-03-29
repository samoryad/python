def my_func(a, b, c):
    """ Функция принимает 3 числа, а выводит сумму наибольших двух из них"""

    my_list = [a, b, c]
    my_list = sum(my_list) - min(my_list)
    print(my_list)


my_func(-5, -10, 25.5)


# Решение от преподавателя №1
def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    try:
        my_list.pop(my_list.index(min(my_list)))
        return sum(my_list)
    except TypeError:
        return 'Enter only a numbers!'


print(my_func(2, 11, -30))


# Решение от преподавателя №2
def my_func(arg1, arg2, arg3):
    return sum(sorted([arg1, arg2, arg3])[1:])


print(my_func(1978, 1, 2))
