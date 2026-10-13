# Read a file, split its content into words, and store them in a list. 
# i. Print the total number of words. 
# ii. Print all unique words.
f = open("demo.txt", "r")
data = f.read()
words = data.split()
print("Total words:", len(words))
unique = set(words)
print("Unique words:", unique)
f.close()