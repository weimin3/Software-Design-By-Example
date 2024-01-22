import json
import sys

def do_add(args):
    assert len(args) == 2
    left = do(args[0])
    right = do(args[1])
    return left + right

def do_abs(args):
    assert len(args) == 1
    val = do(args[0])
    return abs(val)

# dynamic dispatch
def do(expr):
    if isinstance(expr,int):
        return expr

    assert isinstance(expr,list)
    if expr[0] == 'abs':
        return do_abs(expr[1:])
    if expr[0] == 'add':
        return do_add(expr[1:])
    assert False, f"Unknown operation {expr[0]}"

def main():
    assert len(sys.argv) == 2,"Usage:expression.py expr.tll"
    with open(sys.argv[1],'r') as reader:
        program = json.load(reader)
    result = do(program)
    print(f"==> {result}")

if __name__ == '__main__':
    main()

