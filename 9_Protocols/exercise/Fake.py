class Fake:
    def __init__(self,func = None,value= None):
        self.calls = []
        self.func = func
        self.value = value

    def __call__(self,*args,**kwargs):
        self.calls.append([args,kwargs])
        if self.func is not None:
            return self.func(*args,**kwargs)
        return self.value

def fixit(name,func = None, value = None):
    assert name in globals()
    fake = Fake(func,value)
    globals()[name] = fake
    return fake

def adder(a,b):
    return a+b

def test_with_real_function():
    print('--test_with_real_function--')
    print(f'adder(2,3) is {adder(2,3)}')
    assert adder(2,3) == 5

def test_with_fixed_return_value():
    print("--test_with_fixed_return_value--")
    fixit('adder',value = 99)
    print(f'adder(2,3) is {adder(2, 3)}')
    assert adder(2,3) == 99

def test_fake_records_calls():
    fake = fixit('adder',value=99)
    print("--test_fake_records_calls--")
    assert adder(2,3) == 99
    print(f'adder(2,3) is {adder(2, 3)}')
    assert adder(3,4) == 99
    print(f'adder(3,4) is {adder(3, 4)}')
    assert adder.calls == [[(2,3),{}],[(3,4),{}]]
    # print(f'adder.calls is {adder.calls}')

def test_fake_calculates_result():
    print("--test_fake_calculates_result--")
    fixit('adder',func = lambda left,right:10*left + right)
    assert adder(2,3) == 23
    print(f"adder(2,3) is {adder(2,3)}")


def run_test():
    result = {'pass':0,'fail':0,'error':0}
    for name,func in globals().items():
        if not name.startswith('test_'):
            continue

        try:
            func()
            result['pass'] +=1
        except AssertionError:
            result['fail'] +=1
        except Exception:
            result['error'] +=1
    print(f"pass: {result['pass']}")
    print(f"fail: {result['fail']}")
    print(f"error: {result['error']}")

run_test()