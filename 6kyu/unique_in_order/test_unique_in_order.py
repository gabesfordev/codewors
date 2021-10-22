import unittest
from unique_in_order import unique_in_order

class UniqueInOrderTestCase(unittest.TestCase):

    def test_unique_in_order(self):
        self.assertEqual(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])
        self.assertEqual(unique_in_order(''), [])


unittest.main()