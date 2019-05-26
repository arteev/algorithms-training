import unittest
from multi.mul import mul
 
class TestMul(unittest.TestCase):
    def test_small(self):
        self.assertEqual(mul(2,3), 6)
        self.assertEqual(mul(25,25), 625)
        self.assertEqual(mul(2333,30), 2333*30)
        self.assertEqual(mul(30, 2333), 2333*30)

    def test_large(self):
        
        a=2123878
        b=42324
        #89891012472
        self.assertEqual(mul(a,b),a * b )
    
    def test_zeros(self):
        self.assertEqual(mul(0,1), 0)
        self.assertEqual(mul(0,0), 0)
        self.assertEqual(mul(10000,0), 0)

if __name__ == '__main__':
    unittest.main()