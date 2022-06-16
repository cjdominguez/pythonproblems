"""
Implement a class - Student - that has four properties and two methods.

Implement a method – totalObtained – in the Student class that calculates total marks of a student.

Sample properties

name = Mark
phy  = 80
chem = 90
bio  = 40

Using the totalObtained method, implement another method, percentage,
in the Student class that calculates the percentage of students marks
"""

class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio


    def totalObtained(self):
        return(self.phy + self.chem + self.bio)

    def percentage(self):
        return (self.totalObtained()/300*(100))

Mark = Student("Mark", 90, 90, 90)
print(Mark.percentage())



#educatives implementation
class Student1:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):
        return(self.phy + self.chem + self.bio)

    def percentage(self):
        return((self.totalObtained() / 300) * 100)
Mark = Student1("Mark", 90, 90, 90)
print(Mark.percentage())
