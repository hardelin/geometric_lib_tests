import math
import unittest


def area(r):
    if(not(isinstance(r, int) or isinstance(r, float))):
        return False
    return math.pi * r * r


def perimeter(r):
    if(not(isinstance(r, int) or isinstance(r, float))):
        return False
    return 2 * math.pi * r

class CircleTestCases(unittest.TestCase):
    def test_positive_double_area(self):
        res = area(15.45)
        self.assertAlmostEqual(res, 749.906, places=3)
        
    def test_positive_double_perimetr(self):
        res = perimeter(15.45)
        self.assertAlmostEqual(res, 97.075, places=3)
        
    def test_positive_area(self):
        res = area(20)
        self.assertAlmostEqual(res, 1256.637, places=3)
        
    def test_positive_perimetr(self):
        res = perimeter(20)
        self.assertAlmostEqual(res, 125.664, places=3)
        
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
