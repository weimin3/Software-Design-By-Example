import math


def square_perimeter(thing):
    return 4 * thing['side']

def square_area(thing):
    return thing['side'] ** 2

Square = {
    'perimeter':square_perimeter,
    'area': square_area,
    '_classname': 'Square'
}

def square_new(name,side):
    return{
        'name':name,
        'side':side,
        '_class': Square
    }

def cycle_perimeter(thing):
    return 2 * math.pi * thing['radium']

def cycle_area(thing):
    return math.pi * thing['radium'] ** 2

Cycle = {
    'perimeter': cycle_perimeter,
    'area': cycle_area,
    '_classname' : 'Cycle'
}

def cycle_new(name,radium):
    return{
        'name':name,
        'radium':radium,
        '_class': Cycle
    }

def call(thing,method_name):
    return thing['_class'][method_name](thing)

examples = [square_new('sq1',4),cycle_new('ci1',2)]
for thing in examples:
    n = thing['name']
    p = call(thing,'perimeter')
    a = call(thing,'area')
    c = thing['_class']['_classname']
    print(f"{n} is a {c}, perimeter is {p} and area is {a}")
