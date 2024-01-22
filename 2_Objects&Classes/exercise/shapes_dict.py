import math


def square_perimeter(thing):
    return 4 * thing['side']

def square_area(thing):
    return thing['side'] ** 2

def square_new(name,side):
    return{
        'name': name,
        'side': side,
        'perimeter':square_perimeter,
        'area': square_area
    }

def cycle_perimeter(thing):
    return 2 * math.pi *thing['radium']

def cycle_area(thing):
    return math.pi * thing['radium'] ** 2

def cycle_new(name, radium):
    return{
        'name': name,
        'radium': radium,
        'perimeter': cycle_perimeter,
        'area': cycle_area
    }

def call(thing,method_name):
    return thing[method_name](thing)

examples = [square_new('sq',3),cycle_new('ci',2)]
for thing in examples:
    n = thing['name']
    p = call(thing,'perimeter')
    a = call(thing,'area')
    print(f"{n} : {p:.2f}, {a:.2f}")

