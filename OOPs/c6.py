#Constructor, Destructor and @classmethod Demo
class Stud:
    count=0
    def __init__(self, name):
        self.name = name
        Stud.count+=1
        print("Student Created")

    def __del__(self):
        Stud.count -= 1
        print("Student Deleted")

    @classmethod
    def total_students(cls):
        print("Total Objects: ",cls.count)

s1=Stud("Swaraj")
s2=Stud("Shreepad")
s3=Stud("Pravin")
s4=Stud("Harsh")
Stud.total_students()
s2.__del__()
Stud.total_students()