#Multilevel Eg 2
class Student:
    def accept(self):
        self.name=input("Enter name: ")
class Marks(Student):
    def get_marks(self):
        self.marks=float(input("Enter Marks: "))
class Result(Marks):
    def calculate(self):
        if self.marks>=40:
            self.status="Pass"
        else:
            self.status="Fail"
    def display(self):
        print("Name: ",self.name)
        print("Marks: ",self.marks)
        print("Status: ",self.status)
r=Result()
r.accept()
r.get_marks()
r.calculate()
r.display()