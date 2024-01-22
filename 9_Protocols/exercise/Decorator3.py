# def decorator(func,label):
#     def _inner(args):
#         print(f"enter {label}")
#         func(args)
#     return _inner
#
# @decorator('message')
# def double(x):
#     return x * 2


def decorator(func, label):
    def _inner(arg):
        print(f"entering {label}")
        func(arg)
    return _inner

@decorator("message")
def double(x):           # equivalent to
    return 2 * x         # double = decorator(double, "message")


double(3)