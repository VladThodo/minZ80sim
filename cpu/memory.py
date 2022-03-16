# Memmory dummy class

import hexdump


class Memory:

    def __init__(self):
        self.data = bytearray()
        self.current_addr = 0x00

    def load_from_file(self, file):
        byte_array = bytearray(file.read())
        file.close()
        self.data = byte_array
        pass

    def set_starting_address(self, address):
        pass

    def read(self, address):
        pass

    def read_current(self):
        return self.data[self.current_addr]

    def read_next(self):
        pass

    def dump_contents(self):
        print(hexdump.dump(self.data, size=2, sep=' '))

    def read_all(self):
        return self.data

    def __getitem__(self, item):
        return self.data[item]
