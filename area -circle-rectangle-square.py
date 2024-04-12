# Задача №2 с использованием полиморфизма.
#
# Продемонстрировать принцип полиморфизма через реализацию разных классов, представляющих геометрические формы, и метод для расчёта площади каждой формы.
#
# Создать базовый класс Shape с методом area(), который просто возвращает 0.
#
# Создать несколько производных классов для разных форм (например, Circle, Rectangle, Square), каждый из которых переопределяет метод area().
#
# В каждом из этих классов метод area() должен возвращать площадь соответствующей фигуры.
#
# Написать функцию, которая принимает объект класса Shape и выводит его площадь.




class Shape():
    def area (self):
        return 0

class Circle(Shape):
    
    def __init__(self, radius): #переменная
        self.radius = radius #привязываем к классу

    def area(self):
        return 3.14 * self.radius**2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

def print_area(shape):
    print(f"площадь равна {shape.area()}")


circle = Circle(5)
square = Square(7)
rectangle = Rectangle(10, 5)


print_area(circle)
print_area(square)
print_area(rectangle)


















