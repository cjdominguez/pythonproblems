"""
Implement the following properties as private:
name
rollNumber


Include the following methods to get and set the private properties above:
getName()
setName()
getRollNumber()
setRollNumber()

"""


class Student:
    def __init__(self, name = None, rollNumber = None):
        self.__name = name
        self.__rollNumber = rollNumber

    def getName(self):
        return self.__name

    def setName(self,x):
        self.__name = x


    def getRollNumber(self):
        return self.__rollNumber

    def setRollNumber(self,y):
        self.__rollNumber = y


s1 = Student('cj', 1111)
print(s1.getName())
s1.setName('steve')
print(s1.getName())
