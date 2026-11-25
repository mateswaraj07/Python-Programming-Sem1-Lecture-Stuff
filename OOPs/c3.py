# Getters and Setters Demo
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks
    # Getter
    def get_marks(self):
        return self.__marks
    # Setter
    def set_marks(self, marks):
        self.__marks = marks
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.__marks)

# Creating object
s1 = Student("Rahul", 85)
# Accessing private data using getter
print("Old Marks:", s1.get_marks())
# Updating private data using setter
s1.set_marks(95)
# Displaying updated data
print("New Marks:", s1.get_marks())
