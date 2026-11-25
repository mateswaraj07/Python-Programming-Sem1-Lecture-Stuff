#Example 1
class MyClass:
    def __init__(self,name):
        self.name=name
    def print(self):
        return self.name

o=MyClass("Swaraj")
print("Name: ",o.print())