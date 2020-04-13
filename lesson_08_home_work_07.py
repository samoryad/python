class ComplexNumber:
    def __init__(self, param_1):
        self.param_1 = param_1

    def __add__(self, other):
        return self.param_1 + other.param_1

    def __mul__(self, other):
        return complex((self.param_1.real * other.param_1.real - self.param_1.imag * other.param_1.imag),
                       (self.param_1.imag * other.param_1.real + self.param_1.real * other.param_1.imag))

    def __str__(self):
        return f'{self.param_1}'


comp_1 = ComplexNumber(2 + 3j)
comp_2 = ComplexNumber(5 + 4j)
comp_3 = ComplexNumber(5 - 10j)
print(comp_1)
print(comp_1 + comp_2)
print(comp_2 + comp_3)
print(comp_1 * comp_2)
print(comp_1 * comp_3)
