# Read all lines from a file into a list. 
# Print the total number of lines and display the second and 4th line.
f = open("demo.txt", "r")
lines = f.readlines()
print("Total lines:", len(lines))
print("Second line:", lines[1])
print("Fourth line:", lines[3])
f.close()