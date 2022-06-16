"""
Implement a constructor to initialize the values of two private properties: length and width.

Implement a method, area(), in the Rectangle class that returns the product of length and width.
 See the formula below:


Implement a method, perimeter(), in the Rectangle class that returns two times the sum of length and width.
See the formula below:

Perimeter = 2\times (length + width)




class Rectangle:
    def __init__(self, length=0, width=0):
        self.__length = length
        self.__width = width

    def getArea(self):
        return(self.__length*self.__width)

    def getPerimeter(self):
        return(self.getArea() * 2)


p1 = Rectangle(5, 4)
print(p1.getPerimeter())


"""

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return (self.__length * self.__width)

    def perimeter(self):
        return (2 * (self.__length + self.__width))


obj1 = Rectangle(4, 5)
print("Area is", obj1.area())
print("Perimeter is", obj1.perimeter())
