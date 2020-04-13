class MyError(Exception):
    def __init__(self, data):
        self.data = data


user_number = input("Введите делитель: ")
try:
    user_number = int(user_number)
    if user_number == 0:
        raise MyError("Делить на 0 нельзя!")
except MyError as err:
    print(err)
except ValueError:
    print("Вы ввели не число")
else:
    a = round(100 / user_number, 2)
    print(f"Всё хорошо. 100 разделить на {user_number}: {a}")
