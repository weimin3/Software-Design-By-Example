def sign(value):
    if value < 0:
        return -1
    else:
        return 1

def test_sign_negative():
    assert sign(-3) == -1

def test_sign_positive():
    assert sign(19) == 1

def test_sign_zero():
    assert sign(0) == 0

def test_sign_error():
    assert sgn(1) == 1

def run_tests():
    result = {'pass':0,'fail':0,'error':0}
    for name,func in globals().items():
        if not name.startswith('test_'):
            continue
        try:
            func()
            result['pass'] += 1
        except AssertionError:
            result['fail'] += 1
        except Exception:
            result['error'] += 1
    print(f"pass : {result['pass']}")
    print(f"fail : {result['fail']}")
    print(f"error : {result['error']}")

run_tests()