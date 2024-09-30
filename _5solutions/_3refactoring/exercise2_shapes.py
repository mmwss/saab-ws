import math

class Shape:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class RegularPolygon(Shape):
    def __init__(self, side_length, num_sides):
        self.side_length = side_length
        self.num_sides = num_sides

    def perimeter(self):
        return self.side_length * self.num_sides

class Square(RegularPolygon):
    def __init__(self, side_length):
        super().__init__(side_length, 4)

    def area(self):
        return self.side_length ** 2

class EquilateralTriangle(RegularPolygon):
    def __init__(self, side_length):
        super().__init__(side_length, 3)

    def area(self):
        return (math.sqrt(3) / 4) * self.side_length ** 2
