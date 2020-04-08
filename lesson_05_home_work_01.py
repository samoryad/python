try:
    my_file = open('text_file_for_hw_01.txt', 'w', encoding='utf-8')
    while True:
        user_data = input('Введите данные через Ввод, при вводе пустой строки - выход: ')
        if len(user_data) == 0:
            break
        else:
            my_file.write(f'{user_data} \n')
    my_file.close()
except IOError:
    print('Произошла ошибка ввода - вывода!')
