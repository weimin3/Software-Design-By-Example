import json
import sys


def do_add(env,args):
    assert len(args) == 2
    left = do(env,args[0])
    right = do(env,args[1])
    return left + right

def do_abs(env,args):
    assert len(args) == 1
    assert isinstance(args,str)
    val = do(env,args[0])
    return abs(val)

def do_get(env,args):
    assert len(args) == 1
    assert isinstance(args[0],str)
    assert args[0] in env,f"Unknown operation {args[0]}"
    return env[args[0]]

def do_set(env,args):
    assert len(args) == 2
    assert isinstance(args[0],str)
    value = do(env,args[1])
    env[args[0]] = value
    return value

def do_seq(env,args):
    assert len(args) > 0
    for item in args:
        result = do(env,item)
    return result


OPS = {
    name.replace('do_',''):fuc
    for (name,fuc) in globals().items()
    if name.startswith('do_')
}

def do(env,args):
    if isinstance(args,int):
        return args

    assert isinstance(args,list)
    assert args[0] in OPS,f"Unknown operation {args[0]}"
    fuc = OPS[args[0]]
    return fuc(env,args[1:])

def main():
    assert len(sys.argv)==2,"Usage:var_reflect.py filename"
    with open(sys.argv[1],'r') as reader:
        program = json.load(reader)
    result = do({},program)
    print(f"==> {result}")

if __name__ == '__main__':
    main()


