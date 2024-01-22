import math

def shape_density(thing,weight):
    return weight/call(thing,'area')

Shape = {
    'density':shape_density,
    '_classname':'Shape',
    '_parent':None
}

def square_piremeter(thing):
    return 4 * thing['side']

def square_area(thing):
    return thing['side'] ** 2

Square = {
    'piremeter':square_piremeter,
    'area':square_area,
    '_classname':'Square',
    '_parent':Shape
}

def square_new(name,side):
    return{
        'name':name,
        'side':side,
        '_class':Square
    }

def cycle_piremeter(thing):
    return math.pi * 2 * thing['radium']

def cycle_area(thing):
    return math.pi * thing['radium'] ** 2

Cycle = {
    'piremeter': cycle_piremeter,
    'area':cycle_area,
    '_classname':'Cycle',
    '_parent': Shape
}

def cycle_new(name,radium):
    return {
        'name':name,
        'radium':radium,
        '_class':Cycle
    }

def call(thing,method_name,*args):
    method = find(thing['_class'],method_name)
    return method(thing,*args)

def find(cls,method_name):
    while cls is not None:
        if method_name in cls:
            return cls[method_name]
        cls = cls['_parent']
    raise NotImplementedError('method_name')

examples = [square_new('sq',2),cycle_new('ci',3)]
for thing in examples:
    n = thing['name']
    c = thing['_class']['_classname']
    d = call(thing,'density',5)
    p = call(thing,'piremeter')
    a = call(thing,'area')
    print(f"{n} is a {c} , it's density is {d}, perimeter is {d} and area is {a}")