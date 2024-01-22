import math


def square_perimeter(thing):
    return 4 * thing['side']

def square_area(thing):
    return thing['side']**2

def square_larger(thing,size):
    return call(thing,'area') > size

Square = {
    'perimeter':square_perimeter,
    'area':square_area,
    'larger':square_larger,
    '_classname': 'Square'
}

def square_new(name,side):
    return{
        'name':name,
        'side':side,
        '_class':Square
    }

def cycle_piremeter(thing):
    return 2 * math.pi * thing['radium']

def cycle_area(thing):
    return math.pi * thing['radium'] ** 2

def cycle_larger(thing,size):
    return call(thing,'area') > size

Cycle ={
    'perimeter': cycle_piremeter,
    'area':cycle_area,
    'larger':cycle_larger,
    '_classname':'Cycle'
}
def cycle_new(name,radium):
    return{
        'name':name,
        'radium':radium,
        '_class':Cycle
    }

def call(thing,method_name,*args):
    return thing['_class'][method_name](thing,*args)

examples = [square_new('sq',3),cycle_new('ci',2)]
for thing in examples:
    n = thing['name']
    p = call(thing,'perimeter')
    a = call(thing,'area')
    c = thing['_class']['_classname']
    result = call(thing,'larger',5)
    print(f"{n} is {c}, piremeter is {p} and area is {a} , is {n} larger? {result}")

