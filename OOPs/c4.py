
# Using property decorator
class Student:
    def __init__(self):
        self.__marks = 0

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value

s = Student()
s.marks = 80
print(s.marks)
