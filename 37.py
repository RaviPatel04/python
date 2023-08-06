# Method Overriding

class rect:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
    

class circle(rect):

    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)

    def area(self):
        return 3.14 * super().area()
    
# r = rect(2, 3)
# print(r.area())

c = circle(1)
print(c.area())