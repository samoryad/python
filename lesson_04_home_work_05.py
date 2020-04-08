from functools import reduce


def multipl(x, y):
    return x * y


print(reduce(multipl, range(100, 1001, 2)))
