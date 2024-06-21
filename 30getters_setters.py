# Getters and Setters

class Myclass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property
    def getter(self):
        return 13*self._value

    @getter.setter
    def getter(self, newvalue):
        self._value = newvalue/13

obj = Myclass(23)
obj.getter = 65
print(obj.getter)
obj.show()
