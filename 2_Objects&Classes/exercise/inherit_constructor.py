import math

def shape_density(thing,weight):
    return weight/call(thing,'area')

def shape_new(name):
    return{
        'name':name,
        '_class':Shape
    }

Shape = {
    'density': shape_density,
    '_classname':'Shape',
    '_parent': None,
    '_new':shape_new
}

def make(cls,*args):
    return cls['_new'](*args)

def square_perimeter(thing):
    return 4 * thing['side']

def square_area(thing):
    return thing['side'] ** 2

def square_new(name,side):
    return make(Shape,name) | {
        'side':side,
        '_class':Square
    }

Square = {
    'perimeter':square_perimeter,
    'area':square_area,
    '_classname':'Square',
    '_parent':Shape,
    '_new':square_new
}


def circle_perimeter(thing):
    return 2 * math.pi * thing['radium']

def circle_area(thing):
    return math.pi * thing['radium'] ** 2
def circle_new(name,radium):
    return make(Shape,name) | {
        'radium':radium,
        '_class':Circle

    }

Circle = {
    'perimeter':circle_perimeter,
    'area':circle_area,
    '_classname':'Circle',
    '_parent': Shape,
    '_new': circle_new
}

def find(cls,method_name):
    if cls is None:
        raise NotImplementedError('method_name')
    if method_name in cls:
        return cls[method_name]
    return find(cls['_parent'],method_name)


def call(thing,method_name,*args,**kwargs):
    method = find(thing['_class'],method_name)
    return method(thing,*args,**kwargs)



examples = [make(Square,'sq',3),make(Circle,'ci',2)]
for thing in examples:
    n = thing['name']
    c = thing['_class']['_classname']
    p = call(thing,'perimeter')
    a = call(thing,'area')
    d = call(thing,'density',5)
    print(f"{n} is a {c}, the perimeter is {p:.2f} ,the area is {a:.2f} , the density is {d:.2f}")
