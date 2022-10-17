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

def solve(complexOne, complexTwo):
    print(complexOne + complexTwo)
    print(complexOne - complexTwo)
    print(complexOne * complexTwo)
    print(complexOne / complexTwo)

if __name__ == '__main__':
    x = Complex(2, 10)
    y = Complex(3, 5)
    solve(x,y)
    print(x.modulus())
    print(y.modulus())
   