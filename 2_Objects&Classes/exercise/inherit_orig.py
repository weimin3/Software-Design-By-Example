import math


class Shape:
    def __init__(self,name):
        self.name = name

    def piremeter(self):
        raise NotImplementedError('piremeter')

    def area(self):
        raise NotImplementedError('area')

    def density(self,weight):
        return weight/self.area()


class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def piremeter(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2

class Cycle(Shape):
    def __init__(self,name,radium):
        super().__init__(name)
        self.radium = radium

    def piremeter(self):
        return 2 * math.pi * self.radium

    def area(self):
        return math.pi * self.radium ** 2

examples = [Square('sq',3),Cycle('ci',2)]
for thing in examples:
    n = thing.name
    p = thing.piremeter()
    a = thing.area()
    d = thing.density(5)
    print(f"{n} : piremeter is {p} ,area is {a} and density is {d}")
