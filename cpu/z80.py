import sys  # We need those thicc juicy CLI arguments, oh boy

import z80core as core
# We should probaby start by defining the CPU registers

A = 0b10000001  # CPU A register (accumulator - 8 bits)
B = 0b00000000  # CPU B register (general purpose register - 8 bits)
C = 0b00000000  # CPU C register (general purpose register - 8 bits)
PC = 0b000000000000000  # Program counter register 16 bits
SP = 0b00000000  # Stack pointer register
FLAGS = 0b00000000  # CPU flags register, TODO: Write some documentation
HALT = 0

# NOTE: Z80 C & D registers can be grouped into one single 16-bit register


memory_image = None


# CPU Instructions


def help():
    print("Hey, look, someone asked for help")


def dummy_func():
    print("This is a dummy function")


def read_memory_image(image_file):
    # Skeleton function for implementing memory loading
    f = open(image_file, "rb")
    global memory_image
    memory_image = f.read()
    return bytearray(memory_image)


def parse_instruction(function_byte):
    # Try to parse each instruction
    print(function_byte)


def increment_pc():
    global PC  # Go to next address
    PC = PC + 1


def read_next():
    global memory_image
    global PC
    return memory_image[PC + 1]


def read_next_2():
    global memory_image
    global PC
    return memory_image[PC + 2]


def dump_flag_register():
    print("C")
    print(FLAGS >> 0 & 1)


def dump_registers():
    print(f"A: {bin(A)} {hex(A)}")
    print(f"B: {bin(B)} {hex(B)}")
    dump_flag_register()


def finished():
    print(f"Execution finished at addr {hex(PC)}")
    dump_registers()


def run(mem_img):
    # Call this after loading an image
    global PC
    global A
    global FLAGS
    addr = 0
    incPC = 1
    while HALT != 1:
        match mem_img[addr]:
            case 0x00:
                core.nop()
                incPC = 1
            case 0x01:
                ld("BC", 0x00)
                incPC = 1
            case 0x02:
                pass
            case 0x03:
                pass
            case 0x04:
                pass
            case 0x05:
                core.dec('B')
                incPC = 1
            case 0x06:
                core.ld('B', read_next())
                incPC = 1
            case 0x07:              # RLCA
                A = rotate_left(A, 1)
                FLAGS = set_bit(FLAGS, 0)
                incPC = 1
            case 0xC3:
                print("Executed")
                jmp(read_next() | (read_next_2()) << 8)
                incPC = 0
            case 0x76:
                halt = 1
        if PC < len(mem_img) and incPC == 1:
            increment_pc()
            addr = addr + 1
    finished()


if len(sys.argv) > 1:
    if sys.argv[1] == "help":
        help()
    else:
        run(read_memory_image(sys.argv[1]))
else:
    print("There were no arguments. Type help to learn more. Bye.")
