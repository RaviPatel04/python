# Class Methods

class Employee:
    company  = "Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod # This method change company in class Employee
    def changecompany(cls, newcompany):
        cls.company = newcompany

e = Employee()
e.name = "Ravi"
e.show()

e.changecompany("Microsoft")
e.show()
print(Employee.company) #If we run without declare @classmethod grt output is Apple.