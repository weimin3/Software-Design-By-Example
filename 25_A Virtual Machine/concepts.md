- Every computer has a processor with a particular instruction set,some registers, and memory
- Instructions are just numbers but may be represented as assembly code
- Instructions may refer to registers,memory,both or neither
- A processor usually executes instructions in order but may jump to another location
based on whether a conditional is true or false


Virtual Machine simulates a computer with three parts:
- The Instruction pointer(IP) holds the memory address of instruction to execute.It is automaticall
initialized to point to address 0
- Four registers named R0 to R3 that instructions can access directly.There are o 
memory-to-memory operations in VM:everything happens in or through registers
- 256 words of memory,each of which can store a single value.Both the program and 
its data live in this single block of memory; we chose the size 256 so that 
the address of each word will fit in a single byte.

**Instruction set** defines what it can do, instructions are just nembers,
can write them in a simple text format called **assembly code** that give those 
number human-readable names.

the instrutions are 3 bytes long. the op code fits in one byte, and each instruction 
may include zero,one or two single-byte operands.Each operand is a register
identifier, a constant, or an address,which is just a constant that identifies
a location in memory