# Constructors

class college:
    def __init__(self, no, branch):
        print("Hello!!")
        self.enrollment_no = no
        self.branch = branch

    def info(self):
        print(f"{self.enrollment_no} is in  {self.branch}")

a = college(23, "computer engineering")
a.info()

b = college(13, "mechanical engineering")
b.info()