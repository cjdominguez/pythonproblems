"""
add() is a method that returns the sum of num1 and num2.

subtract() is a method that returns the subtraction of num1 from num2.

multiply() is a method that returns the product of num1 and num2.

divide() is a method that returns the division of num2 by num1.
"""

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


    def add(self):
        return(self.num1 + self.num2)

    def subtract(self):
        return(self.num2 - self.num1)

    def multiply(self):
        return(self.num1  * self.num2)

    def divide(self):
        return(self.num2 / self.num1)


answer = Calculator(10, 94)
print(answer.add())
print(answer.subtract())
print(answer.multiply())
print(answer.divide())
