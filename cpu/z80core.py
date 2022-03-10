# Z80 core CPU functions
# Probably not the best way of implementing this, but it works

from eeprom import EEPROM


###################
#    CPU FLAGS    #
###################

class Z80Core:

    def __init__(self):
        # Init CPU registers
        self.A = 0
        self.B = 0
        self.C = 0
        self.D = 0

        self.PC = 0  # Program counter
        # CPU flags
        self.FLAGZ = 0  # Zero flag
        self.FLAGC = 0  # Carry flag
        self.FLAGH = 0  # Halt flag

        # Init memory
        self.ROM = EEPROM()

    def dump_registers(self):
        print(f"A: {bin(self.A)} {hex(self.A)}")
        print(f"B: {bin(self.B)} {hex(self.B)}")
        print(f"C: {bin(self.C)} {hex(self.C)}")

    def dump_flags(self):
        print(f"C: {self.FLAGC}")
        print(f"Z: {self.FLAGZ}")

    def set_carry_flag(self):
        self.FLAGC = 1

    def reset_carry_flag(self):
        self.FLAGC = 0

    def set_zero_flag(self):
        self.FLAGZ = 1

    def reset_zero_flag(self):
        self.FLAGZ = 0

    def set_halt_flag(self):
        self.FLAGH = 1

    def reset_cpu(self):
        self.PC = 0
        self.FLAGH = 0
        self.run()

    def parse_instructions(self):
        instruction = self.ROM.read(0x00)  # Start reading at address 0x00
        match instruction:
            case 0x00:
                pass
            case 0x76:
                pass

    def run(self):
        if self.FLAGH == 0:
            self.finish()
        pass

    def finish(self):
        self.dump_registers()
        self.dump_flags()

    # Instruction set for the CPU

    def nop(self):
        pass

    def halt(self):
        pass

    def ld(self, register, value):
        pass

    def inc(self, register):
        match register:
            case 'A':
                self.A += 1
            case 'B':
                self.B += 1
            case 'C':
                self.C += 1
            case 'D':
                self.D += 1

    def dec(self, register):
        match register:
            case 'A':
                self.A -= 1
            case 'B':
                self.B -= 1
            case 'C':
                self.C -= 1
            case 'D':
                self.D -= 1

    def write_io(self, port_address):
        pass

    def read_io(self, port_address):
        pass
