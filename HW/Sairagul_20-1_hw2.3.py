def gcd(a,b):
    while a%b != 0:
        oldm = a
        oldn = b

        a = oldn
        b = oldm % oldn

    return b


class Fraction:
    def __init__(self, numerator, denumerator):
        self.numerator = numerator
        self.denumerator = denumerator

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denumerator)

    def __add__(self, other):
        newnum = self.numerator * other.denumerator + self.denumerator * other.numerator
        newden = self.denumerator * other.denumerator
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __sub__(self, other):
        newnum = self.numerator * other.denumerator - self.denumerator * other.numerator
        newden = self.denumerator * other.denumerator
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __mul__(self, other):
        res1 = (self.numerator * other.numerator)
        res2 = self.denumerator * other.denumerator
        common = gcd(res1, res2)
        return Fraction(res1 // common, res2 // common)

    def __floordiv__(self, other):
        res1 = (self.numerator * other.denumerator)
        res2 = self.denumerator * other.numerator
        common = gcd(res1, res2)
        return Fraction(res1 // common, res2 // common)

x = Fraction(1,2)
y = Fraction(2,3)
print(f'Sum of two fractions: {x + y}')
print(f"Substriction of two fractions: {x-y}")
print(f'Multiplication of two fractions: {x*y}')
print(f'Division of two fractions: {x//y}')