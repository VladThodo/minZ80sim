import sys  # We need those thicc juicy CLI arguments, oh boy

from z80core import Z80Core

cpu = Z80Core()

if len(sys.argv) > 1:
    if sys.argv[1] == "help":
        help()
    else:
        print("Yes there are arguments but I don't care.")
else:
    print("There were no arguments. Type help to learn more. Bye.")
    cpu.inc('A')
    cpu.inc('C')
    cpu.dump_registers()
