import unittest
from jaden_casing_strings import to_jaden_case

class JadenCasingStringsTestCase(unittest.TestCase):
    def test_to_jaden_case(self):
        
        quote = "How can mirrors be real if our eyes aren't real"
        self.assertEqual(to_jaden_case(quote), "How Can Mirrors Be Real If Our Eyes Aren't Real")

unittest.main()