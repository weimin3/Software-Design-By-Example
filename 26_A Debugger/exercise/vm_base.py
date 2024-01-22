import sys
from architecture import NUM_REG,OP_MASK,OP_SHIFT,OPS,RAM_LEN,VMState

COLUMNS = 4
DIGITS = 8

class VirtualMachineBase:
    @classmethod
    def main(cls):
        #run a program and show the result
        assert len(sys.argv) == 2,f"Usage: {sys.argv[0]} program"
        with open(sys.argv[1],'r') as reader:
            lines = [ln.strip() for ln in reader.readlines()]
        program = [int(ln,16) for ln in lines if ln]
        vm = cls()
        vm.initialize(program)
        vm.run()
        vm.show()

    def __init__(self,writer = sys.stdout):
        self.writer = writer
        self.initialize([])

    def initialize(self,program):
        assert len(program)<=RAM_LEN,"Program is too long for memory"
        self.ram = [program[i] if len(program)<i else 0 for i in range(RAM_LEN)]
        self.ip = 0
        self.reg = [0] * NUM_REG

    def run(self):
        self.state = VMState.RUNNING
        while self.state != VMState.FINISHED:
            addr,op,arg0,arg1 = self.fetch()
            self.execute(op,arg0,arg1)

    def fetch(self):
        # get the next instruction
        assert(
            0<=self.ip<len(self.ram)
        ),f"Program counter {self.ip:06x} out of range 0..{len(self.ram):06x}"
        old_ip = self.ip
        instruction = self.ram[self.ip]
        self.ip +=1
        return(old_ip,*self.decode(instruction))

    def decode(self,instruction):
        # decode an instruction to get an op code and its operands
        op = instruction & OP_MASK
        instruction >>= OP_SHIFT
        arg0 = instruction & OP_MASK
        instruction >>= OP_SHIFT
        arg1 = instruction & OP_MASK
        return op,arg0,arg1

    def execute(self,op,arg0,arg1):
        # execute a single instruction
        if op == OPS["hlt"]["code"]:
            self.state = VMState.FINISHED

        elif op == OPS["ldc"]["code"]:
            self.assert_is_register(arg0)
            self.reg[arg0] = arg1

        elif op == OPS["ldr"]["code"]:
            self.assert_is_register(arg0)
            self.assert_is_register(arg1)
            self.reg[arg0] = self.ram[self.reg[arg1]]

        elif op == OPS["cpy"]["code"]:
            self.assert_is_register(arg0)
            self.assert_is_register(arg1)
            self.reg[arg0] = self.reg[arg1]

        elif op == OPS["str"]["code"]:
            self.assert_is_register(arg0)
            self.assert_is_register(arg1)
            self.assert_is_address(self.reg[arg1])
            self.ram[self.reg[arg1]] = self.reg[arg0]

        elif op == OPS["add"]["code"]:
            self.assert_is_register(arg0)
            self.assert_is_register(arg1)
            self.reg[arg0] += self.reg[arg1]

        elif op == OPS["sub"]["code"]:
            self.assert_is_register(arg0)
            self.assert_is_register(arg1)
            self.reg[arg0] -= self.reg[arg1]

        elif op == OPS["beq"]["code"]:
            self.assert_is_register(arg0)
            self.assert_is_address(arg1)
            if self.reg[arg0] == 0:
                self.ip = arg1

        elif op == OPS["bne"]["code"]:
            self.assert_is_register(arg0)
            self.assert_is_address(arg1)
            if self.reg[arg0] != 0:
                self.ip = arg1

        # [prr]
        elif op == OPS["prr"]["code"]:
            self.assert_is_register(arg0)
            self.write(f"{self.reg[arg0]:06x}")
        # [/prr]

        elif op == OPS["prm"]["code"]:
            self.assert_is_register(arg0)
            self.assert_is_address(self.reg[arg0])
            self.write(f"{self.ram[self.reg[arg0]]:06x}")

        else:
            assert False, f"Unknown op {op:06x}"

    def assert_is_register(self,reg):
        assert 0 <= reg < len(self.reg),f"Invalid register {reg:06x}"

    def assert_is_address(self,addr):
        assert 0 <= addr < len(self.ram),f"Invalid address {addr:06x}"

    def write(self,*args):
        msg = "".join(args) + '\n'
        self.writer.write(msg)

    def show(self):
        # show the ip,register and memory
        self.write(f"IP{' ' * 6} = {self.ip:06x}")
        for (i,r) in enumerate(self.reg):
            self.write(f"R{i:06X} = {r:06x}")

        # how much memory to show
        top = max(i for (i,m) in enumerate(self.ram) if m != 0)

        base = 0
        while base<= top:
            output = f"{base:06x}"
            for i in range(COLUMNS):
                output += f"  {self.ram[base + i]:06x}"
            self.write(output)
            base += COLUMNS
         
if __name__ == '__main__':
    VirtualMachineBase.main()