# Reverse the accepted string
s = input("Enter a String: ")
print("Reversed String: ", s[::-1])
 #OR
rev = ""
for char in s:
    rev = char + rev
print(rev) #We take each character from the string and 
           #add it before the existing reversed string, so the characters appear in reverse order