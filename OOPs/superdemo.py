class A:
    def show(self):
        print("Class A")

class B:
    def show(self):
        print("Class B")
        super().show()

class C(A, B):
    def show(self):
        print("Class C")
        super().show()

obj = C()
obj.show()