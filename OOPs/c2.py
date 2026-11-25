#Types of Data Members Demo
class Student:

    # Class member
    college = "ABC College"

    def __init__(self, name, roll_no, marks):
        # Instance members
        self.name = name
        self.roll_no = roll_no

        # Private data member
        self.__marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("College:", Student.college)
        print("Marks:", self.__marks)


# Creating objects (instances)
s1 = Student("Rahul", 101, 85)
s2 = Student("Priya", 102, 90)

# Displaying student details
s1.display()
print()

s2.display()
