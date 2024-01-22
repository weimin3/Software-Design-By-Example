from struct import pack,unpack

def pack_string(as_string):
    as_bytes = bytes(as_string,'utf-8')
    header = pack('i',len(as_bytes))
    format = f'{len(as_bytes)}s'
    body = pack(format,as_bytes)
    return header + body

def unpack_string(buffer):
    header,body = buffer[:4],buffer[4:]
    length = unpack('i',header)[0]
    format =f'{length}s'
    result = unpack(format,body)[0]
    return str(result,'utf-8')

buffer = pack_string("hello!")
result = unpack_string(buffer)
print(result)