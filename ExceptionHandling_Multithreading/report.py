#printing report
roll = int(input("Enter your roll number: "))
name= input("Enter your name: ")
marks = float(input("Enter your marks: "))
try:
    if marks <0 or marks>100:
        raise ValueError("Marks should be between 0 and 100.")
    if marks>=75:
        grade = 'A'
    elif marks>=60:
        grade = 'B'
    elif marks>=40:
        grade = 'C'
    else:
        grade = 'F'
except ValueError as ve:
    print("Error:", ve)
else:
    print("\nReport Card")
    print("Roll Number:", roll)
    print("Name:", name)
    print("Marks:", marks)
    print("Grade:", grade)