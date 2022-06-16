class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        print(self.x**2 + self.y**2 + self.z**2)

Total = Point(1, 3, 5)
Total.sqSum()



class Points:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        a = (self.x**2)
        b = (self.y**2)
        c = (self.z**2)
        return(a+b+c)


target = Points(4, 5, 6)
print(target.sqSum())
