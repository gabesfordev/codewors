import unittest
from complementary_dna import DNA_strand

class DNATestCase(unittest.TestCase):
    def test_DNA_strand(self):
        self.assertEqual(DNA_strand("AAAA"),"TTTT","String AAAA is")
        self.assertEqual(DNA_strand("ATTGC"),"TAACG","String ATTGC is")
        self.assertEqual(DNA_strand("GTAT"),"CATA","String GTAT is")

unittest.main()