import unittest

from z80core import Z80Core


class InitTest(unittest.TestCase):
    def test_init(self):
        self.cpu = Z80Core()

    def test_init_registers(self):
        self.cpu = Z80Core()
        self.assertEqual(self.cpu.A, 0)
        self.assertEqual(self.cpu.B, 0)
        self.assertEqual(self.cpu.C, 0)
        self.assertEqual(self.cpu.D, 0)



if __name__ == '__main__':
    unittest.main()
