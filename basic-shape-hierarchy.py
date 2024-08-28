class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return None

import math

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

def print_area(shape):
    print(f"The area of the {shape.name} is: {shape.area()}")

# Instantiate objects
rectangle = Rectangle(5, 10)
circle = Circle(7)

# Call the print_area function for each object
print_area(rectangle)
print_area(circle)
