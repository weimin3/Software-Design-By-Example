def wrap(label):
    def decorator(func):
        def _inner(*args):
            print(f"befor call {label}")
            func(*args)
            print(f"after call {label}")
        return _inner
    return decorator

@wrap("wrapping")
def original(message):
    print(f"original: {message}")

original('example')