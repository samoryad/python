class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')
        print(self.title)

class Pen(Stationery):
    def draw(self):
        print('Ручка draw')
        print(self.title)

class Pencil(Stationery):
    def draw(self):
        print('Карандаш draw')
        print(self.title)

class Handle(Stationery):
    def draw(self):
        print('Маркер draw')
        print(self.title)


s = Stationery('канцтовары')
s.draw()
print(s.title)

pen = Pen('ручка')
pen.draw()

pencil = Pencil('карандаш')
pencil.draw()

h = Handle('маркер')
h.draw()
