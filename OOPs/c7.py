class Student:
    def __init__(self):
        self.__marks = 0

    # Getter
    @property
    def marks(self):
        return self.__marks

    # Setter
    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid marks!")


# Creating object
s = Student()

# Setting value
s.marks = 80

# Getting value
print("Marks:", s.marks)