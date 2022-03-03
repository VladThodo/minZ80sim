# Z80 core CPU functions

def nop():
    pass


def jmp(addr):
    global PC
    PC = addr


def inc(reg):
    pass


def dec(reg):
    global A
    global B
    match reg:
        case 'A':
            A = A - 1
        case 'B':
            B = B - 1


def rotate_left(x, n):      # Thank you StackOverflow
    return int(f"{x:032b}"[n:] + f"{x:032b}"[:n], 2)


def set_bit(value, bit):        # Thank you StackOverflow again
    return value | (1 << bit)


def write_to_mem(addr, val):
    pass


def ld(reg, val):
    global A
    global B
    match reg:
        case 'A':
            A = val
        case 'B':
            B = val
        case 'C':
            pass
        case 'D':
            pass
        case "BC":
            pass
        case "SP":
            SP = val
