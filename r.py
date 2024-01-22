def make(thing):
    def _inner():
        return thing

    def a():
        return  thing +1

    return _inner,a



 b = make(1+2)
print(b[1]())
