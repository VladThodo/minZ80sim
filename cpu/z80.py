import sys  # We need those thicc juicy CLI arguments, oh boy

from z80core import Z80Core
from eeprom import EEPROM

cpu = Z80Core()

if len(sys.argv) > 1:
    if sys.argv[1] == "help":
        help()
    else:
        file = open(sys.argv[1], 'rb')  # Read binary ROM image
        rom = EEPROM()
        rom.load_from_file(file)
        cpu.set_rom(rom)
        rom.dump_contents()
        cpu.run()
else:
    print("There were no arguments. Type help to learn more. Bye.")
