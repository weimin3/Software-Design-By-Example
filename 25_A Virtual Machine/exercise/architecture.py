# number of registers
NUM_REG = 4
# number of words in RAM
RAM_LEN = 256

OPS = {
    'hlt':{'code':0x1,'fmt':'--'},
    'ldc':{'code':0x2,'fmt':'rv'},
    'ldr':{'code':0x3,'fmt':'rr'},
    'cpy':{'code':0x4,'fmt':'rr'},
    'str':{'code':0x5,'fmt':'rr'},
    'add':{'code':0x6,'fmt':'rr'},
    'sub':{'code':0x7,'fmt':'rr'},
    'beq':{'code':0x8,'fmt':'rv'},
    'ben':{'code':0x9,'fmt':'rv'},
    'prr':{'code':0xA,'fmt':'r-'},
    'prm':{'code':0xB,'fmt':'r-'},
}

#select a single byte
OP_MASK = 0XFF

#shift up by one byte
OP_SHIFT = 8

#op width in characters when printing
OP_WIDTH = 6