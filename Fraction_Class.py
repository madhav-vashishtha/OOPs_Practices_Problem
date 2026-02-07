class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        self.numerator = numerator
        self.denominator = denominator
        self._simplify()

    def _gcd(self, a, b):
        a = abs(a)
        b = abs(b)
        while b != 0:
            a, b = b, a % b
        return a

    def _simplify(self):
        gcd = self._gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def add(self, other):
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def subtract(self, other):
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def multiply(self, other):
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def divide(self, other):
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero")
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Fraction(num, den)

    def __eq__(self, other):
        return (self.numerator == other.numerator and
                self.denominator == other.denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction(numerator={self.numerator}, denominator={self.denominator})"

frac1 = Fraction(1, 2)
frac2 = Fraction(3, 4)

print(frac1.add(frac2))    
print(frac1.subtract(frac2)) 
print(frac1.multiply(frac2)) 
print(frac1.divide(frac2))    

print(frac1 == Fraction(2, 4)) 
print(frac1)                 

#print(frac1.divide(Fraction(0, 1))) 

