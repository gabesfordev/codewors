import unittest
from add_length import add_length

class AddLengthTestCase(unittest.TestCase):
    """Tests for add_length.py"""

    def test_word_length(self):
        self.assertEqual(add_length('apple ban'), ["apple 5", "ban 3"])

unittest.main()