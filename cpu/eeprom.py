# We'll use this to load program our program memory

from memory import Memory


class EEPROM(Memory):

    def size(self):
        return len(self.data)
