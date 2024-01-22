# square and cycle have the same methods and can use them interchangeably, this is called polymorphism.
import math

# this is a contract
class Shape:
    # constructor method
    def __init__(self,name):
        self.name = name
    # subclass inheriting from Shape need to overwrite this method
    def perimeter(self):
        raise NotImplementedError("perimeter")

    def area(self):
        raise NotImplementedError("area")

class Square(Shape):
    # constructor
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2

class Cycle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2


examples = [Square('sq',3),Cycle('ci',2)]
for thing in examples:
    n = thing.name
    p = thing.perimeter()
    a = thing.area()
    print(f"{n} has perimeter {p:.2f} and area {a:.2f}")


