# dir, __dict__ and help method

print("dir method")
x = [1, 2, 3]
print(dir(x))

print("\n__dict__ method")
class person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

p = person("Ravi", 19, 100000)
print(p.__dict__)

print("\nhelp method")
print(help(person))