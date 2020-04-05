from math import factorial
""" первое решение через import factorial"""


def fibo_gen(n):
    yield factorial(n)


print(fibo_gen(10))
for el in fibo_gen(15):
    print(el)


""" второе через import цикл (вывод до введённого числа)"""


def fact(n):
    factorial_01 = 1
    for i in range(2, n + 1):
        if i > n:
            break
        else:
            factorial_01 *= i
            print(factorial_01)
    yield factorial_01


print(fact(5))
enter = int(input('Введите число, от которого нужно взять факториал: '))
for elem in fact(enter):
    print(f'факториал {enter} равен: {elem}')
