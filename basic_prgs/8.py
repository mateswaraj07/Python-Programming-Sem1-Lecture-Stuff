#list (Mutable)
students = ["Vaibhav", "Swaraj", "Shreepad"]
print("List of students:", students)
students.append("Om") #add new student
print(students)
print("First student:", students[0]) #access first student

#Range datatype
#simple
for i in range(5):
    print(i)

for i in range(2, 7):
    print(i)

#in step 3
print("In step 3")
for i in range(1, 10, 3):
    print(i)

#count down
print("Count down")
for i in range(5, 0, -1):
    print(i)


#Tuple (Immutable)
students = ("Vaibhav", "Swaraj", "Shreepad")
print("Tuple of students:", students)
print("First student:", students[0])