from memory import Memory


class RAM(Memory):

    def __init__(self, size):
        super().__init__()
        self.size = size
        self.data = bytearray(self.size)

    def write(self, contents, addr):
        self.data[addr] = contents
