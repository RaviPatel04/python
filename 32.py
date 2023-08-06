# Access Modifiers
# by default public access

# private (use __ to create)

class Employee: 
    def __init__(self):
        self.__name = "sun"



e = Employee()
# print(e.__name) #cannot access directly 
print(e._Employee__name)