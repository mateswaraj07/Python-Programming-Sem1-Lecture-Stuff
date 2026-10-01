""" 2. Searching and Counting Methods in Python str

These methods are used to search for a word/character inside a string or count how many times it appears."""

# 1. find()

# Definition: Finds the first position (index) of a substring. If it is not found, it returns -1.

text = "hello world"

print(text.find("o"))

# Output: 4

# 👉 "o" first appears at index 4.

# 2. rfind()

#Definition: Finds the last position (index) of a substring. If it is not found, it returns -1.

text = "hello world"

print(text.rfind("o"))

# Output: 7

# 👉 "o" appears at indexes 4 and 7, so rfind() gives 7.

# 3. index()

# Definition: Finds the first position (index) of a substring. If it is not found, it gives an error.

text = "hello world"

print(text.index("o"))

# Output: 4

# If we write:

# print(text.index("z"))

# It gives an error: ValueError

"""👉 Difference from find():

find() → returns -1
index() → gives an error """

# 4. rindex()

# Definition: Finds the last position (index) of a substring. If it is not found, it gives an error.

text = "hello world"

print(text.rindex("o"))

# Output: 7

# 👉 "o" appears at indexes 4 and 7, so rindex() gives 7.

"""👉 Difference from rfind():

rfind() → returns -1
rindex() → gives an error"""

# 5. count()

# Definition: Counts how many times a substring appears in a string.

text = "hello world"

print(text.count("o"))

# Output: 2

# 👉 "o" appears 2 times.

"""Easy trick:
r = reverse/right side → last occurrence
find = search safely
index = search, but error if missing
count = how many times"""