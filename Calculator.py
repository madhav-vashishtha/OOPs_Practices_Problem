class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self, factor):
        return self.num1 * factor
    
    def divide(self, divisor):
        if divisor == 0:
            print("Error: Cannot divide by zero")
            return None
        return self.num1 / divisor
    
calculator = Calculator(45,5)

print("Addition Result:", calculator.add())
print("Subtraction Result:", calculator.subtract())
print("Multiplication Result:", calculator.multiply(3))
print("Division Result", calculator.divide(2))
print("Division Result:", calculator.divide(0))


