class MyError(Exception):
    def __init__(self, data):
        self.data = data


my_list = []
while True:
    user_data = input('Введите целое положительное число. Для выхода из программы нажмите "Q": ')
    if user_data.upper() == 'Q':
        break
    else:
        try:
            if user_data.isdigit() is False:
                raise MyError('Данные введены некорректно, введите целое положительное число: ')
            else:
                my_list.append(int(user_data))
        except MyError as err:
            print(err)
print(f'Итоговый список корректно введённых чисел: {my_list}')
