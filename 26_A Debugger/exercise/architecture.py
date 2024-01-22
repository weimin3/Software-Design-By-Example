from enum import Enum

OPS = {
    "hlt": {"code": 1, "fmt": "--"},  # Halt program
    "ldc": {"code": 2, "fmt": "rv"},  # Load immediate
    "ldr": {"code": 3, "fmt": "rr"},  # Load register
    "cpy": {"code": 4, "fmt": "rr"},  # Copy register
    "str": {"code": 5, "fmt": "rr"},  # Store register
    "add": {"code": 6, "fmt": "rr"},  # Add
    "sub": {"code": 7, "fmt": "rr"},  # Subtract
    "beq": {"code": 8, "fmt": "rv"},  # Branch if equal
    "bne": {"code": 9, "fmt": "rv"},  # Branch if not equal
    "prr": {"code": 10, "fmt": "r-"},  # Print register
    "prm": {"code": 11, "fmt": "r-"},  # Print memory
    "brk": {"code": 15, "fmt": "--"},  # Breakpoint
}

OP_MASK = 0XFF
OP_SHIFT = 8
OP_WIDTH = 6

NUM_REG = 4
RAM_LEN = 256

class VMState(Enum):
    FINISHED = 0
    STEPPING = 1
    RUNNING = 2