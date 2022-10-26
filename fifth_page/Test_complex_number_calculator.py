import unittest



class Complex:
    def __init__(self, real, imag):
        self.r = real
        self.i = imag

    def __add__(self, o):
        return Complex(self.r + o.r, self.i + o.i)

    def __sub__(self, o):
        return Complex(self.r - o.r, self.i - o.i)

    def __mul__(self, o):
        return Complex(self.r * o.r - self.i * o.i, self.r * o.i + self.i * o.r)

    def __truediv__(self, o):
        m = o.r * o.r + o.i * o.i
        return Complex((self.r * o.r + self.i * o.i)/m, (self.i * o.r - self.r * o.i)/m)

    def modulus(self):
        return (pow(pow(self.r,2) + pow(self.i,2) , 1/2))
        
    def __str__(self):
        if self.i == 0:
            return '%.2f' % self.r
        if self.r == 0:
            return '%.2fi' % self.i
        if self.i < 0:
            return '%.2f - %.2fi' % (self.r, -self.i)
        else:
            return '%.2f + %.2fi' % (self.r, self.i)


def splitEquation(equation):
    values = []
    actualString = ""
    for i in equation:
        print(i)
        if i == ")":
            values.append(actualString)
            actualString = ""
        elif i == "(":
            continue
        else:
            actualString += i
    if actualString != "":
        values.append(actualString)
    print(values)
    return values

def simpleCalculator():
    number = Complex(0, 0)
    sign = ""
    x = ""
    while True:
        print("Enter number or cancel(c): ")
        x = input()
        if x == "c":
            break
        complex = getComplexNumber(x)
        if sign == "":
            number =  complex
        elif sign == "+":
            number += complex
            sign = ""
        elif sign == "-":
            number -= complex
            sign = ""
        elif sign == "*":
            number *= complex

            sign = ""
        elif sign == "/":
            try:
                number /=complex
            except ZeroDivisionError:
                print("Cannot divide by 0")
                return
            sign = ""
        print("Enter operation sign:")
        sign = input()
        if sign == "=":
            break

    if x == "c":
        return

    else:
        print("Result: " + str(number))

def getComplexNumber(text):
    real = ""
    img = ""
    waitForImaginary = False
    text = text.replace(" ","")

    for i in text:
        if i == "i":
            break
        if i == "+" or i == "-":
            waitForImaginary = True
        if (i != "+" or i != "-") and not waitForImaginary:
            real = real+i
        elif waitForImaginary:
            img = img+i

    if real == "+" or real == "-" or real == "*" or real == "/":
        real = "0"
        img = "0"

    if ("i" in text) and img == "":
        img = str(real)
        real = "0"

    elif img == "":
        img = "0"
    return Complex(int(real), int(img))

def solve(equation):
    splitted = []
    values = splitEquation(equation)

    for i in values:
        splitted.append(str(i).split())
    result = Complex(0, 0)
    strongerSign = ""
    for i in splitted:
        localComplex = Complex(0, 0)
        sign = ""
        for j in i:
            if j != "*" and j != "/" and j != "+" and j != "-":
                if localComplex.real == 0 and localComplex.imag == 0:
                    localComplex = getComplexNumber(j)
                if sign == "+":
                    localComplex.__add__(getComplexNumber(j))
                    sign = ""
                if sign == "-":
                    localComplex.__sub__(getComplexNumber(j))
                    sign = ""
                if sign == "*":
                    localComplex.__mul__(getComplexNumber(j))
                    sign = ""
                if sign == "/":
                    try:
                        localComplex.__div__(getComplexNumber(j))
                    except ZeroDivisionError:
                        print("Cannot divide by 0")
                        return
                    sign = ""
            else:
                sign = j
    return result 

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
    #simpleCalculator()