# Inheritance

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def detail(self):
        print(f"Employee name : {self.name}\nEmployee id : {self.id}")

class programmer(Employee):
    def langauge(self):
        print(f"Employee know a langaue is : ptyhon")

e = Employee("Royal",  3)
e.detail()

e1 = programmer("Roy", 33)
e1.detail()
e1.langauge()