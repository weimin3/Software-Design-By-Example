class Fake:
    def __init__(self,func = None,value = None):
        self.func = func
        self.value = value

    def __call__(self,*args,**kwargs):
        if self.func is not None:
            return self.func(*args,**kwargs)
        return self.value

class ContextFake(Fake):
    def __init__(self,name,func = None,value = None):
        super().__init__(func,value)
        self.name = name
        self.original = None

    def __enter__(self):
        assert self.name in globals()
        self.original = globals()[self.name]
        globals()[self.name] = self
        return self

    def __exit__(self,exc_type,exc_value,exc_traceback):
        globals()[self.name] = self.original

def subber(a,b):
    return a - b

def check_no_lasting_effects():
    assert subber(2,3) == -1
    print(f"1:subber(2,3) is {subber(2,3)}")

    with ContextFake('subber',value = 1234) as fake:
        print(f"2:subber(2,3) is {subber(2, 3)}")
        assert subber(2,3) == 1234

    assert subber(2, 3) == -1
    print(f"3:subber(2,3) is {subber(2, 3)}")

check_no_lasting_effects()