class Data:
    def __init__(self, date):
        self.date = date

    @classmethod
    def take_date(cls, str_date):
        my_list = str_date.split('-')
        new_list = []
        for num in my_list:
            new_list.append(int(num))
        if Data.date_check(new_list):
            print(f'Данные проверены, числа даты можно увидеть в списке: {new_list}')
        else:
            print('Дата введена некорректно')

    @staticmethod
    def date_check(some_list):
        for el in range(len(some_list)):
            if 0 < some_list[0] < 31:
                if 0 < some_list[1] < 12:
                    if 0 < some_list[2] <= 20:
                        return True


d = Data('10-04-20')
d.take_date('10-04-20')
d.take_date('18-06-15')
d.take_date('22-04-20')
d.take_date('40-04-20')
