def original(value):
    print(f"original : {value}")

def logging(func,label):
    def __inner(value):
        print(f"++ {label}")
        func(value)
        print(f"--{label}")
    return __inner




original = logging(original,'call')
original('example')