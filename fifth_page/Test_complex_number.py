import unittest
from complex_number import Complex

class TestComplexCalculator(unittest.TestCase):
    def testAddComplexNumber(self):
        a = Complex(2, 5)
        b = Complex(2, 5)
        result = a.__add__(b)
        test = Complex(4, 10)
        y = result.modulus()
        x = test.modulus()
        self.assertAlmostEquals(x,y)

    def testSubComplexNumber(self):
        a = Complex(9, 3)
        b = Complex(2, 5)
        result = a.__sub__(b)
        test = Complex(7, -2)
        y = result.modulus()
        x = test.modulus()
        self.assertAlmostEquals(x,y)

    def testMulComplexNumber(self):
        a = Complex(3, 5)
        b = Complex(2, 4)
        result = a.__mul__(b)
        test = Complex(-14, 22)
        y = result.modulus()
        x = test.modulus()
        self.assertAlmostEquals(x,y)

    def testDivComplexNumber(self):
        a = Complex(4, 4)
        b = Complex(2, 2)
        result = a.__truediv__(b)
        test = Complex(2,0)
        y = result.modulus()
        x = test.modulus()
        self.assertAlmostEquals(x,y) 

if __name__ == '__main__':
    unittest.main()  
