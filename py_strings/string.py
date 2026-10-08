# demonstarte all string functions / methods in python
text = input("Enter a string: ")
# strip -> it removes whitespace from the beginning and end of the string
print("Original string:", text)
print("String after strip:", text.strip())
# capitalize -> it capitalizes the first character of the string
print("String after capitalize:", text.capitalize())
# lower -> it converts all characters of the string to lowercase
print("String after lower:", text.lower())
# upper -> it converts all characters of the string to uppercase
print("String after upper:", text.upper())
# title -> it capitalizes the first character of each word in the string
print("String after title:", text.title()) # capitaize() capitalizes only the first character of the string, 
# while title() capitalizes the first character of each word in the string.
#count -> it counts the number of occurrences of a substring in the string
substring = input("Enter a substring to count: ")
print("Number of occurrences:", text.count(substring))
# find -> it returns the index of the first occurrence of a substring in the string. If the substring is not found, it returns -1.
substring = input("Enter a substring to find: ")
print("Index of first occurrence:", text.find(substring))
# replace -> it replaces all occurrences of a substring with another substring
new = input("Enter a substring to replace: ")
print("String after replace:", text.replace(text, new))
# startswith -> it checks if the string starts with a specified substring. It returns True if it does, and False otherwise.
substring = input("Enter a substring: ")
print("Result of startswith:", text.startswith(substring))
# endswith -> it checks if the string ends with a specified substring. It returns True if it does, and False otherwise.
substring = input("Enter a substring: ")
print("Result of endswith:", text.endswith(substring))
# split -> it splits the string into a list of substrings based on a specified word. The default word is whitespace.
substring = input("Enter a word to split by: ")
print("List of substrings:", text.split(substring))
# join -> it joins a list of strings into a single string, with a specified separator between each string.
separator = input("Enter a separator: ")
print("Joined string:", separator.join(text.split(substring)))
# isalpha -> it checks if all characters in the string are alphabetic. It returns True if they are, and False otherwise.
print("Result of isalpha:", text.isalpha())
# isdigit -> it checks if all characters in the string are digits. It returns True if they are, and False otherwise.
print("Result of isdigit:", text.isdigit())
# swapcase -> it swaps the case of all characters in the string. Uppercase characters become lowercase, and lowercase characters become uppercase.
print("String after swapcase:", text.swapcase())
# partition -> it splits the string into three parts: the part before the specified substring, the substring itself, and the part after the substring. It returns a tuple containing these three parts.
substring = input("Enter a substring to partition by: ")
print("Partitioned parts:", text.partition(substring))
 # expand() is used to replace tabs with spaces. It takes an optional argument tabsize, which specifies the number of spaces to replace each tab with. The default value of tabsize is 8.
substring = input("Enter a substring to expand: ")
print("String after expand:", text.expand(tabsize=4))