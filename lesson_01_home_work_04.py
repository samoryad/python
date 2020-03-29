user_number = int(input('введите целое положительное число: '))
number = 0
if user_number >= 0:
    while user_number != 0:
        if number < user_number % 10:
            number = user_number % 10
        user_number = user_number // 10
    print('максимальная цифра в числе:',number)
else:
    print('введено отрицательное цисло')
