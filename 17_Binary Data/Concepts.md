**UTF-32**: Stores every character as a 32-bit number, may waste lots of memory
**UTF-8** which is variable length
**why should we store data in formats that people can't easily read?**
- **size**
- **Speed**
- **Lack of anything better**

If we open a file for reading using open('filename','r') then Python assumes we
want to read character strings from file. It therefore:
- asks the operating system for the default character encoding(always UTF-8)
- uses this to convert bytes to characters
- converts Windows end-of-Line markers to the Unix standard if necessary.(行尾标记符的转化)
Windows uses both a carriage return '\r' and a newline '\n' to mark the end of a line,while
Unix uses only the latter('\n')

A Python list, store reference to values rather than the values themselves.

**Packing data**: the format string specifies what types of data are being packed
how big they are, how many values they are, how much memory is required

**Unpacking**: 
- after reading data into memory, unpack it according to format
- the most important thing is that we can unpack data any way we want(pack
 an integer and unpack it as four characters)

Python's **struct** module packs and unpacks data for us, 
- the function `pack(format,val_1,val_2,...)`
takes a format string, and packs them into a bytes object
- the function `unpack(format,string)` takes some bytes and a format and return 
a tuple containing the unpacked values.

what is something like **\x1f**?
- if Python finds a byte in a string that doesn't correspond to a printable character,
it prints a 2-digit escape sequence(2位转义序列) in hexadecimal.