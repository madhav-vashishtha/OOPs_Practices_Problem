class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, other):
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary
        return ComplexNumber(real_part, imaginary_part)
    
    def subtract(self, other):
        real_part = self.real - other.real
        imaginary_part = self.imaginary - other.imaginary
        return ComplexNumber(real_part, imaginary_part)
    
    def multiply(self, other):
        real_part = (self.real * other.real) - (self.imaginary * other.imaginary)
        imaginary_part = (self.real * other.imaginary) + (self.imaginary * other.real)
        return ComplexNumber(real_part, imaginary_part)
    
    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary
    
    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {abs(self.imaginary)}i"
        
# Creating instances
c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(1, 4)

# Addition
print("Addition Result:", c1.add(c2))       

# Subtraction
print("Subtraction Result:", c1.subtract(c2)) 

# Multiplication
print("Multiplication Result:", c1.multiply(c2)) 

# Equality check
print("Equality Test:", c1 == ComplexNumber(2, 3)) 
