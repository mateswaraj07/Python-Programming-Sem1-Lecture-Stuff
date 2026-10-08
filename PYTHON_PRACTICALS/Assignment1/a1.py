# Create a dictionary with students details
students = {
    101 : {"Name":"Swaraj", "Scores":[80,85,90]},
    102: {"Name":"Shreepad","Scores":[78,82,87]},
    103: {"Name":"Vaibhav","Scores":[88,72,77]},
    104: {"Name":"Pravin","Scores":[79,90,67]},
    105: {"Name":"Om","Scores":[28,29,30]}
}
print(students)
print()
# Calulate average score and flag pass / fail
for sid, details in students.items():
    avg = sum(details['Scores']) / len(details["Scores"])
    details["Average"] = avg
    details["Passed"] = avg >= 50
print(students)
print()
#Print names of students who passed
print("Students who passed:")
for sid, details in students.items():
    if details["Passed"]:
        print(details["Name"])


# Taking values from the user

# students = {}

# num_students = int(input("Enter the number of students: "))

# for _ in range(num_students):
#     student_id = int(input("\nEnter Student ID: "))
#     name = input("Enter Student Name: ")
    
#     # Prompt for 3 specific scores
#     score1 = int(input("Enter Score 1: "))
#     score2 = int(input("Enter Score 2: "))
#     score3 = int(input("Enter Score 3: "))
    
#     students[student_id] = {
#         "Name": name,
#         "Scores": [score1, score2, score3]
#     }

# print("\nFinal Students Dictionary:")
# print(students)