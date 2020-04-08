import math


class Cell:
    def __init__(self, cell_sectors):
        self.cell_sectors = cell_sectors
        self.sectors_in_row = 5

    def __add__(self, other):
        return Cell(self.cell_sectors + other.cell_sectors)

    def __sub__(self, other):
        if self.cell_sectors < other.cell_sectors:
            print('Первая клетка слишком мала для вычитания')
        else:
            return Cell(self.cell_sectors - other.cell_sectors)

    def __mul__(self, other):
        return Cell(self.cell_sectors * other.cell_sectors)

    def __truediv__(self, other):
        try:
            return Cell(math.floor(self.cell_sectors / other.cell_sectors))
        except ZeroDivisionError:
            print('В клетке не может быть 0 ячеек')

    def __str__(self):
        return str(self.cell_sectors)

    def make_order(self, sectors_in_row):
        my_list = []
        while self.cell_sectors >= sectors_in_row:
            my_list.append(str('*' * sectors_in_row))
            self.cell_sectors -= sectors_in_row
        else:
            my_list.append('*' * self.cell_sectors)
        return '\n'.join(my_list)

    # можно просто принтануть
    # def make_order(self, sectors_in_row):
    #     while self.cell_sectors >= sectors_in_row:
    #         print(str('*' * sectors_in_row))
    #         self.cell_sectors -= sectors_in_row
    #     else:
    #         print('*' * self.cell_sectors)


c_1 = Cell(78)
c_2 = Cell(22)
print(f'Сложили две клетки. Всего ячеек в новой клетке: {c_1 + c_2}')
print(f'Вычли из первой клетки вторую. Всего ячеек в новой клетке: {c_1 - c_2}')
print(f'Размножили клетки. Всего ячеек в новой клетке: {c_1 * c_2}')
print(f'Разделили клетки. Всего ячеек в новой клетке: {c_1 / c_2}')
print(f'{c_2.cell_sectors} ячейки по рядам: ')
print(c_2.make_order(15))
print(f'{c_1.cell_sectors} ячейки по рядам: ')
print(c_1.make_order(17))
