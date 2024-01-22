**Parser**: translates the source code into a data structure
**Runtime**: executes the instructions in that data structure
**Dynamic dispatch**: lookup-and-call process
**Recursion**: a function call itself either directly or indirectly
**expressions**: produce values **statements** don't

**lookup table** is created by **introspection**
```commandline
OPS = {
    name.replace('do_',''):fuc
    for (name,fuc) in globals().items()
    if name.startswith('do_')

}
```