def first():
    print('First')

def second():
    print('Second')

def third():
    print('Third')

everything = [first,second,third]
for e in everything:
    e()