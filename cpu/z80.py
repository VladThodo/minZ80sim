import sys  # We need those thicc juicy CLI arguments, oh boy

from z80core import Z80Core
from eeprom import EEPROM

cpu = Z80Core()


def show_help():
    pass


if len(sys.argv) > 1:
    if sys.argv[1] == "help":
        show_help()
    else:
        file = open(sys.argv[1], 'rb')  # Read binary ROM image
        rom = EEPROM()
        rom.load_from_file(file)
        cpu.set_rom(rom)
        print("Machine code to execute: ")
        rom.dump_contents()
        print("\n")
        cpu.run()
else:
    print("There were no arguments. Type help to learn more. Bye.")
