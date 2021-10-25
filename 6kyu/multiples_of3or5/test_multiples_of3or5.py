import unittest
from multiples_of3or5 import solution

class MultiplesOf3or5TestCase(unittest.TestCase):

    def test_multipels_of_3or(self):
        self.assertEqual(solution(4), 3)        
        self.assertEqual(solution(6), 8)    
        self.assertEqual(solution(16), 60)    
        self.assertEqual(solution(3), 0)    
        self.assertEqual(solution(5), 3)    
        self.assertEqual(solution(15), 45)    
        self.assertEqual(solution(0), 0)    
        self.assertEqual(solution(-1), 0)    
        self.assertEqual(solution(10), 23)        
        self.assertEqual(solution(20), 78)
        self.assertEqual(solution(200), 9168)

unittest.main()