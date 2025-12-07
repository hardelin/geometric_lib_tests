import unittest

def area(a):
    return a * a


def perimeter(a):
    return 4 * a

class SqareTestCases(unittest.TestCase):
    def test_positive_double_area(self):
        res = area(15.45)
        self.assertAlmostEqual(res, 238.7025)
        
    def test_positive_double_perimetr(self):
        res = perimeter(15.45)
        self.assertAlmostEqual(res, 61.8)
        
    def test_positive_area(self):
        res = area(20)
        self.assertEqual(res, 400)
        
    def test_positive_perimetr(self):
        res = perimeter(20)
        self.assertEqual(res, 80)
        
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
        
    def test_zero_perimetr(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_negative_lenght_area(self):
        res = area(-5)
        self.assertFalse(res)
        
    def test_negative_lenght_perimetr(self):
        res = perimeter(-5)
        self.assertFalse(res)
        
    def test_string_area(self):
        res = area("test")
        self.assertFalse(res)
        
    def test_string_perimetr(self):
        res = perimeter("test")
        self.assertFalse(res)

