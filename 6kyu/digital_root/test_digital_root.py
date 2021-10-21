import unittest
from digital_root import digital_root

class DigitalRootTestCase(unittest.TestCase):

    def test_digital_root(self):
        self.assertEqual(digital_root(16), 7)
        self.assertEqual(digital_root(942), 6)
        self.assertEqual(digital_root(132189), 6)
        self.assertEqual(digital_root(493193), 2)

unittest.main()