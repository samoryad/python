class Road:

    def __init__(self, _length, _width, m=25, h=5):
        self._length = float(_length)
        self._width = float(_width)
        self.m = m
        self.h = h

    def calculator_volume_road(self):
        return self._length * self._width * self.m * self.h / 1000


calc = Road(5000, 20)
print(f'Масса асфальта будет: {calc.calculator_volume_road()} т')
