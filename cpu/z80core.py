# Z80 core CPU functions
# Probably not the best way of implementing this, but it works

from eeprom import EEPROM


class Z80Core:

    # Instruction set for the CPU

    def nop(self):
        pass

    def halt(self):
        self.set_halt_flag()

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

    def rlca(self):
        pass

    def rrca(self):
        pass

    def deca(self):
        self.A = (self.A - 1) & 0xff
        self.check_for_zero('A')

    def decb(self):
        self.B = (self.B - 1) & 0xff
        self.check_for_zero('B')

    def decc(self):
        self.C = (self.C - 1) & 0xff
        self.check_for_zero('C')

    def decd(self):
        self.D = (self.D - 1) & 0xff
        self.check_for_zero('D')

    def inca(self):
        self.A = (self.A + 1) & 0xff

    def incb(self):
        self.B = (self.B + 1) & 0xff

    def incc(self):
        self.C = (self.C + 1) & 0xff

    def incd(self):
        self.D = (self.D + 1) & 0xff

    def jmp(self, addr):    # Absolute jump
        self.PC = addr

    def jr(self, amount):   # Relative jump
        self.PC += amount

    def rla(self):
        pass

    def write_io(self, port_address):
        pass

    def read_io(self, port_address):
        pass

    def check_for_zero(self, reg):
        match reg:
            case 'A':
                if self.A == 0:
                    self.set_zero_flag()
            case 'B':
                if self.B == 0:
                    self.set_zero_flag()
            case 'C':
                if self.C == 0:
                    self.set_zero_flag()
            case 'D':
                if self.D == 0:
                    self.set_zero_flag()

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

        self.immediate_value = 0

        # Init memory
        self.ROM = EEPROM()

        # Instruction-function mapping in a dictionary

        self.instruction_dict = {
            0x00: self.nop,
            0x01: self.not_defined,
            0x02: self.not_defined,
            0x03: self.not_defined,
            0x04: self.incb,
            0x05: self.decb,
            0x06: self.ld,
            0x07: self.rlca,
            0x08: self.not_defined,
            0x09: self.not_defined,
            0x0A: self.ld,
            0x0B: self.not_defined,
            0x0C: self.incc,
            0x0D: self.decc,
            0x0E: self.ld,
            0x0F: self.rrca,
            0x10: self.not_defined,
            0x11: self.not_defined,
            0x12: self.not_defined,
            0x13: self.not_defined,
            0x14: self.incd,
            0x15: self.decd,
            0x16: self.ld,
            0x17: self.rla,
            0x18: self.jr,
            0x19: self.not_defined,
            0x1A: self.not_defined,
            0x1B: self.not_defined,
            0x76: self.halt
        }

    def set_rom(self, rom: EEPROM):
        self.ROM = rom

    def dump_registers(self):
        format_str = '#010b'
        print(f"A: {format(self.A, format_str)} {hex(self.A)}")
        print(f"B: {format(self.B, format_str)} {hex(self.B)}")
        print(f"C: {format(self.C, format_str)} {hex(self.C)}")
        print(f"D: {format(self.D, format_str)} {hex(self.D)}")
        print(f"PC: {format(self.PC, format_str)} {hex(self.PC)}")

    def dump_flags(self):
        print(f"Carry: {self.FLAGC}")
        print(f"Zero: {self.FLAGZ}")

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

    def not_defined(self):
        pass

    def parse_instructions(self, instruction):
        self.instruction_dict[instruction]()

    def inc_pc(self, step=1):
        self.PC += step

    def run(self):
        if self.FLAGH == 1:
            print("CPU halted.")
            self.finish()
        else:
            while self.FLAGH != 1 and self.PC < len(self.ROM.read_all()):
                self.parse_instructions(self.ROM.read_all()[self.PC])
                self.inc_pc()
            self.finish()
        pass

    def finish(self):
        self.dump_registers()
        self.dump_flags()

