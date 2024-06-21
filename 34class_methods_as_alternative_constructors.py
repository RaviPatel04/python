# Class Methods as Alternative Constructors 

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(self, string):
        return self(string.split("-")[0], string.split("-")[1])
        

string = "Ravi-100000"
e = Employee.fromstr(string)
print(e.name)
print(e.salary)