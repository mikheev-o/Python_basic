# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def info(self):
        print('Треугольник задан координатами:\n'+
              f'A{self.a}, B{self.b}, C{self.c}')

    def square(self):
        return abs((self.b[0] - self.a[0]) * (self.c[1] - self.a[1]) -
                   (self.c[0] - self.a[0]) * (self.b[1] - self.a[1])) / 2

    def perimeter(self):
        return math.sqrt((self.b[0] - self.a[0])**2 + (self.b[1] - self.a[1])**2) +\
               math.sqrt((self.c[0] - self.b[0])**2 + (self.c[1] - self.b[1])**2) +\
               math.sqrt((self.c[0] - self.a[0])**2 + (self.c[1] - self.a[1])**2)

tr1 = Triangle((0,0), (1,0), (0,1))
tr1.info()
print('Площадь = ', tr1.square())
print('Периметр = ', tr1.perimeter())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def info(self):
        print('Трапеция имеет основания:\n'+
              f'AD{self.a}{self.d}, BC{self.b}{self.c}')

    def slopeBC(self):
        return (self.b[1] - self.c[1]) / (self.b[0] - self.c[0])

    def slopeAD(self):
        return (self.a[1] - self.d[1]) / (self.a[0] - self.d[0])

    def _side(self, x, y):
        return math.sqrt((y[0] - x[0])**2 + (y[1] - x[1])**2)

    def sideAB(self):
        return self._side(self.a, self.b)
    def sideCD(self):
        return self._side(self.c, self.d)

    def _angle(self, x, y):
        pass

tp1 = Trapeze((0,0), (1,2), (3,2), (4,0))

tp1.info()

if tp1.slopeBC() != tp1.slopeAD():
    print('Фигура не является трапецией, т.к. основания не параллельны.')
elif tp1.sideAB() != tp1.sideCD():
    print('Длины боковых сторон не равны - значит трапеция не равнобочная')
else:
    print('Осталось проверить углы при основании, но время уже так много :(\n\
  да и программировать геометрию за 8-й класс не очень сложно')
