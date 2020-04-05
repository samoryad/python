with open('text_file_for_hw_05.txt', 'w+', encoding='utf-8') as my_file:
    my_file.write(input('Введите несколько чисел через пробел и нажмите "enter": '))
    try:
        my_file.seek(0)
        content = my_file.readline()
        content = content.split()
        total = 0
        for el in content:
            total += int(el)
        print(f'Сумма введённых чисел равна: {total}')
    except ValueError:
        print('Введите пожалуйста целые числа')
