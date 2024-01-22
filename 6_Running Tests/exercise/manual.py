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

def run_test(all_tests):
    result = {'pass': 0, 'fail': 0, 'error': 0}
    for test in all_tests:
        try:
            test()
            result['pass'] += 1
        except AssertionError:
            result['fail'] += 1
        except Exception:
            result['error'] += 1
    print(f"pass {result['pass']}")
    print(f"fail {result['fail']}")
    print(f"error {result['error']}")

all_tests = [
    test_sign_negative,
    test_sign_positive,
    test_sign_zero,
    test_sign_error
]

run_test(all_tests)
