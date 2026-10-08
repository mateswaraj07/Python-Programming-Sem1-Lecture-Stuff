# 1. consider your name and print all possible meaningful names.
# 2. consider your name and replace all vowels with letter 'z'.
# 3. create a list of numbers and strings, accept the values from user. Seperate the list from the max number. Display the names in descending order.
# 4. accept numbers and store their cubes in the list.

# Q1 Solution
name = "swaraj"
words = ["swara", "swar", "raj"]
for word in words:
    for char in word:
        # If any letter appears more times in 'word' than in 'swaraj'
        if word.count(char) > name.count(char):
            break
    else:
        # Runs only if the loop finished without breaking (word is valid)
        print(word)

# Q2 Solution
name = "Swaraj"
for v in "aeiouAEIOU":
    name = name.replace(v, "z")
print(name)

# Q3 Solution
n = int(input("Enter number of values: "))

numbers = []
names = []

for i in range(n):
    num = int(input("Enter number: "))
    name = input("Enter name: ")

    numbers.append(num)
    names.append(name)

max_num = max(numbers)

print("Maximum number:", max_num)

names.sort(reverse=True)

print("Names in descending order:")
for name in names:
    print(name)


# Q4 Solution
n = int(input("How many elements do you want to enter: "))
l = []

for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    l.append(num ** 3)

print("Cubes of the numbers you entered:")
print(l)