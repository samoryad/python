from copy import deepcopy


class Matrix:
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

    def __getitem__(self, index):
        return self.matrix[index]

    def __add__(self, other):
        other = Matrix(other)
        result = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summa = other[i][j] + self.matrix[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.matrix):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix_1)
print()
matrix_2 = Matrix([[5, 26, 1], [-6, 48, -100], [7, 8, 9]])
print(matrix_2)
print()
print(matrix_1 + matrix_2)
