# Z80 core CPU functions
# Probably not the best way of implementing this, but it works

from eeprom import EEPROM
from ram import RAM

class Z80Core:

    # Instruction set for the CPU

    def nop(self):
        pass

    def ldbc(self):
        pass

    def ldbc_addr(self):
        pass

    def incb(self):
        self.B = (self.B + 1) & 0xff

    def decb(self):
        self.B = (self.B - 1) & 0xff
        self.check_for_zero('B')

    def ldb(self):
        self.B = self.immediate_value

    def rlca(self):
        pass

    def exaf(self):
        pass

    def add_hl_bc(self):
        pass

    def lda_bc_addr(self):
        pass

    def decbc(self):
        pass

    def incc(self):
        self.C = (self.C + 1) & 0xff

    def decc(self):
        self.C = (self.C - 1) & 0xff
        self.check_for_zero('C')

    def ldc(self):
        pass

    def rrca(self):
        pass

    def djnz(self):
        pass

    def ldde(self):
        pass

    def ldde_a(self):
        pass

    def incde(self):
        pass

    def decd(self):
        self.D = (self.D - 1) & 0xff
        self.check_for_zero('D')

    def ldd(self):
        self.D = self.immediate_value

    def rla(self):
        pass

    def jr(self, amount):  # Relative jump
        self.PC += amount

    def add_hl_de(self):
        pass

    def lda_de(self):
        pass

    def dec_de(self):
        pass

    def ince(self):
        pass

    def dece(self):
        pass

    def lde(self):
        pass

    def lda(self):
        self.A = self.immediate_value

    def ldhl(self):
        self.HL = self.immediate_value

    def lda_pointer(self):
        self.A = self.ROM[self.immediate_value]

    def ldba(self):
        self.B = self.A

    def ldda(self):
        self.D = self.A

    def ldmema(self):
        self.RAM.write(self.A, self.immediate_value)

    def rra(self):
        pass

    def jp_z(self):     # Jump if Z flag is set, useful for multiplication
        if self.FLAGZ == 1:
            self.PC = int.from_bytes(self.jp_address, "big")
        else:
            self.PC += 3

    def halt(self):
        self.set_halt_flag()

    def ld(self, register, value):
        pass

    def deca(self):
        self.A = (self.A - 1) & 0xff
        self.check_for_zero('A')

    def inca(self):
        self.A = (self.A + 1) & 0xff

    def incd(self):
        self.D = (self.D + 1) & 0xff

    def jp(self):    # Absolute jump
        self.PC = int.from_bytes(self.jp_address, "big")
        # print(f"Jumped at address {self.PC}")

    def incbc(self):
        pass

    def addab(self):
        self.A = (self.A + self.B) & 0xff

    def addaa(self):
        self.A = (self.A + self.A) & 0xff

    def subb(self):
        self.A = (self.A - self.B) & 0xff
        self.check_for_zero('A')

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
        self.HL = 0

        self.PC = 0  # Program counter
        # CPU flags
        self.FLAGZ = 0  # Zero flag
        self.FLAGC = 0  # Carry flag
        self.FLAGH = 0  # Halt flag

        self.immediate_value = 0
        self.pc_step = 1
        self.jp_address = 0
        # Init memory
        self.ROM = EEPROM()
        self.RAM = RAM(128)

        self.ram_start_addr = 0

        # Instruction-function mapping in a dictionary

        self.instruction_dict = {
            0x00: self.nop,
            0x01: self.not_defined,
            0x02: self.not_defined,
            0x03: self.not_defined,
            0x04: self.incb,
            0x05: self.decb,
            0x06: self.ldb,
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
            0x16: self.ldd,
            0x17: self.rla,
            0x18: self.jr,
            0x19: self.not_defined,
            0x1A: self.not_defined,
            0x1B: self.not_defined,
            0x21: self.ldhl,
            0x32: self.ldmema,
            0x47: self.ldba,
            0x57: self.ldda,
            0xC3: self.jp,
            0xCA: self.jp_z,
            0x3E: self.lda,
            0x3A: self.lda_pointer,
            0x80: self.addab,
            0x87: self.addaa,
            0x90: self.subb,
            0x76: self.halt
        }

    def set_rom(self, rom: EEPROM):
        self.ROM = rom

    def set_ram(self, ram: RAM, start_addr):
        self.RAM = ram
        self.ram_start_addr = 0

    def dump_registers(self):
        format_str = '#010b'
        print(f"A: {format(self.A, format_str)} {hex(self.A)} {self.A}")
        print(f"B: {format(self.B, format_str)} {hex(self.B)}")
        print(f"C: {format(self.C, format_str)} {hex(self.C)}")
        print(f"D: {format(self.D, format_str)} {hex(self.D)}")
        print(f"HL: {format(self.HL, format_str)} {hex(self.HL)}")
        print(f"PC: {format(self.PC, format_str)} {hex(self.PC)}")

    def dump_flags(self):
        print(f"Carry: {self.FLAGC}")
        print(f"Zero: {self.FLAGZ}")
        print(f"Halt: {self.FLAGH}")

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

    def load_immediate(self):
        self.immediate_value = self.ROM[self.PC + 1]
        self.pc_step = 2

    def load_immediate_two_bytes(self):
        data = bytearray(bytes([self.ROM[self.PC + 2]]))
        data.append(self.ROM[self.PC + 1])
        self.immediate_value = int.from_bytes(data, "big")
        self.pc_step = 3

    def load_jp_address(self):
        addr = bytearray(bytes([self.ROM[self.PC + 2]]))
        addr.append(self.ROM[self.PC + 1])
        self.jp_address = addr
        self.pc_step = 0

    def run(self):
        while self.FLAGH != 1 and self.PC < len(self.ROM.read_all()):

            self.pc_step = 1
            match self.ROM[self.PC]:
                case 0x06:          # Load B, immediate
                    self.load_immediate()
                case 0x16:          # Load D, immediate
                    self.load_immediate()
                case 0x3E:
                    self.load_immediate()
                case 0xC3:
                    self.load_jp_address()
                case 0xCA:
                    self.load_jp_address()
                case 0x21:
                    self.load_immediate_two_bytes()
                case 0x3A:
                    self.load_immediate_two_bytes()
                case 0x32:
                    self.load_immediate_two_bytes()

            self.parse_instructions(self.ROM[self.PC])
            if self.PC != len(self.ROM.read_all()) - 1:
                self.inc_pc(self.pc_step)
        self.finish()

    def finish(self):
        self.dump_registers()
        self.dump_flags()
        self.RAM.dump_contents()

