# super keyword

class college:
    
    def detail(self, name, en_no):
        self.name = name
        self.en_no = en_no

    def show(self):
        print(f" name : {self.name}\n en_no : {self.en_no}\n branch : {self.b}")

class branch(college):

    def detailbranch(self, name, en_no, b):
        self.b = b
        super().detail(name, en_no)
        super().show()


b = branch()
b.detailbranch("Ravi", "23", "computer")
