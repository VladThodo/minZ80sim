import argparse  # Baaaaby parse do-do-do-do-do-dooooo
from z80core import Z80Core
from eeprom import EEPROM
from ram import RAM

cpu = Z80Core()

parser = argparse.ArgumentParser(description="Emulate a Z80 microprocessor")
parser.add_argument('-f', type=str, help='The binary file to execute')

args = parser.parse_args()

if args.f:
    file = open(args.f, 'rb')  # Read binary ROM image
    rom = EEPROM()
    ram = RAM(64)
    rom.load_from_file(file)
    cpu.set_rom(rom)
    cpu.set_ram(ram, len(rom.read_all()))
    print("Machine code to execute: ")
    rom.dump_contents()
    print("\n")
    cpu.run()

