#Getter + Setter
class Stud:
    def __init__(self):
        self.__marks=0

    def get_marks(self):
        return self.__marks

    def set_marks(self,marks):
        self.__marks=marks

s=Stud()
print("Before Setting marks are: ",s.get_marks())
s.set_marks(95)
print("After Modification marks are: ",s.get_marks())