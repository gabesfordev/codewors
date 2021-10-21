import unittest
from did_she_say_hello import validate_hello

class DidSheSayHello(unittest.TestCase):

    def test_greetings(self):
        self.assertEqual(validate_hello('hello'), True)
        self.assertEqual(validate_hello('ciao bella!'), True)
        self.assertEqual(validate_hello('salut'), True)
        self.assertEqual(validate_hello('hallo, salut'), True)
        self.assertEqual(validate_hello('hombre! Hola!'), True)
        self.assertEqual(validate_hello('Hallo, wie geht\'s dir?'), True)
        self.assertEqual(validate_hello('AHOJ!'), True)
        self.assertEqual(validate_hello('czesc'), True)
        self.assertEqual(validate_hello('meh'), False)
        self.assertEqual(validate_hello('Ahoj'), True)

unittest.main()