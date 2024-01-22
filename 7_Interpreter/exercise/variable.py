import json
import sys

def do_abs(env,args):
    assert len(args) == 1
    val = do(env,args[0])
    return abs(val)

def do_add(env,args):
    assert len(args) == 2
    left = do(env,args[0])
    right = do(env,args[1])
    return left + right

def do_get(env,args):
    print('there is do_get')
    assert len(args) == 1
    print(f"args is {args}")
    assert isinstance(args[0],str)
    assert args[0] in env, f"Unknown variable {args[0]}"
    return env[args[0]]

def do_seq(env,args):
    print('there is do_seq')
    assert len(args) > 0
    print(f"args is {args}")
    for item in args:
        result = do(env,item)
    return result

def do_set(env,args):
    print('there is do_set')
    assert len(args) == 2
    print(f"args is {args}")
    assert isinstance(args[0],str)
    value = do(env,args[1])
    env[args[0]] = value
    return value



def do(env,args):
    if isinstance(args,int):
        return args
    if args[0] == 'add':
        return do_add(env, args[1:])
    if args[0] == 'abs':
        return do_abs(env, args[1:])
    if args[0] == 'get':
        return do_get(env, args[1:])
    if args[0] == 'set':
        return do_set(env, args[1:])
    if args[0] == 'seq':
        return do_seq(env, args[1:])
    assert False, f"Unknown operation {args[0]}"

def main():
    assert len(sys.argv) == 2,"Usage variable.py filename"
    with open(sys.argv[1],'r') as reader:
        program = json.load(reader)
    result = do({},program)
    print(f"==> {result}")

if __name__ == '__main__':
    main()


