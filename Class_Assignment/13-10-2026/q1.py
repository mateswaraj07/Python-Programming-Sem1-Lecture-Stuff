# Write a program to read a file and count how many vowels are present in the content
f = open("myfile.txt","r")
data = f.read()
count = 0
for ch in data:
    if ch.lower() in "aeiou":
        count+=1
print("Total Vowels: ",count)
f.close()