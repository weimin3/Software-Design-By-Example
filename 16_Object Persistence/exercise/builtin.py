def save(writer,thing):
    if isinstance(thing,bool):
        print(f"Bloon:{thing}",file = writer)

    elif isinstance(thing,float):
        print(f"float: {thing}",file = writer)

    elif isinstance(thing,int):
        print(f"int: {thing}",file = writer)

    elif isinstance(thing,str):
        lines = thing.split('\n')
        print(f"str: {len(lines)}",file = writer)
        for line in lines:
            print(line,file = writer)

    elif isinstance(thing,list):
        print(f"list : {len(thing)}",file = writer)
        for item in thing:
            save(writer,item) #recursive

    elif isinstance(thing,set):
        print(f"set:{len(thing)}", file = writer)
        for item in thing:
            save(writer,item)

    elif isinstance(thing,dict):
        print(f"dict: {len(thing)}",file = writer)
        for (key,value) in thing.items():
            save(writer,key)
            save(writer,value)
    else:
        raise ValueError(f"unknown type of thing {type(thing)}")

def load(reader):
    line = reader.readerline()[:-1]
    assert line,"Nothing to read"
    fields = line.split(":",maxsplit = 1)
    assert len(fields) == 2,f"Badly-formed line {line}"
    key,value = fields

    if key == 'bool':
        name = {'True':True,'False': False}
        assert value in name,f"Unknown Boolean {value}"
        return name[value]

    elif key == 'float':
        return float(value)

    elif key == 'int':
        return int(value)

    elif key == 'list':
        return [load(reader) for _ in range(int(value))]

    elif key == 'str':
        lines = [reader.readline()[:-1] for _ in range(int(value))]
        return "\n".join(lines)

    elif key == 'set':
        return {load(reader) for _ in range(int(value))}

    elif key == 'dict':
        result = {}
        for _ in range(int(value)):
            k = load(reader)
            v = load(reader)
            result[k]=v
        return result

    else:
        raise ValueError(f"unknown type of thing {line}")

