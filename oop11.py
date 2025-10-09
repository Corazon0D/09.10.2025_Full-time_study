# Основные понятия в ООП
# Абстракция

from abc import ABC, abstractmethod


class Shape(ABC):  # абстрактный базовый класс
    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, w, h):
        self._w = w
        self._h = h

    def area(self):
        return self._w * self._h

    def perimeter(self):
        return 2 * (self._w + self._h)

