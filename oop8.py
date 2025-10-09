# оСНОВНЫЕ ПОНЯТИЯ ООП
# Наследование (inheritance)
# Базовый класс (superclass, родительский)
# Производный
class Rectangle:

    def __init__(self, a=1, b=1):
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @a.setter
    def a(self, new_a):
        if not isinstance(new_a, int):
            raise TypeError(f'Сторона прямоугольника должна быть целым числом')
        self._a = new_a

    @b.setter
    def b(self, new_b):
        if not isinstance(new_b, int):
            raise TypeError(f'Сторона прямоугольника должна быть целым числом')
        self._b = new_b

    def __str__(self):
        return f'<{self.__class__.__name__}({self._a}, {self._b})'

    def __repr__(self):
        return f'<{self.__class__.__name__}({self._a}, {self._b})'
        # или return self._a * self._b

    def perimeter(self):
        return 2 * (self._a + self._b)


class Square(Rectangle):
    def __init__(self, a=1):
        super().__init__(a, a)

import math
class Triangle(Square):
    # def __repr__(self, a=1): # Я ПИСАЛ
    #     super().__init__(a, a, a)

    def __init__(self, side):
        if not isinstance(side, (int, float)) or side < 0:
            raise ValueError('Сторона должна быть положительным числом')
        self.side = side # Сохраняем строку
        super().__init__(side) # скорее всего не используем

    def perimeter(self):
        return 3 * self.side

    def ploshad(self, side):
        return (math.sqrt(3) * side ** 2) / 4

    def __str__(self):
        return f'<{self.__class__.__name__}({self.side}, {self.side}, {self.side})'


s = Square(4)
print(s)
print(s.perimeter())

t = Triangle(5)
print(t)
print(t.ploshad(5))
print(t.perimeter())