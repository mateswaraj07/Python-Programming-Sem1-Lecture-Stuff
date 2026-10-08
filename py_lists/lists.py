# 1. Create a list of 10 numbers print the sum of last 4 elements of the list. 
# 2. Find out the difference between maximum and minimum elements of the list. 
# 3. Insert an item in the list at 6th position, this number must be 1/3rd of number stored at 4th position.

# Q1 Solution:
l = [1,2,3,4,5,6,7,8,9,10]
print("List: ",l)
print("Sum of last four elements: ", end="")
sum = 0
for i in l[6:len(l)]:
    sum += i
print(sum)

# Q2 Solution:
l = [1,2,3,4,5,6,7,8,9,10]
print("List: ",l)
print("Max element from the list: ", max(l))
print("Min element from the list: ", min(l))
print("Difference between Max and Min element from the list: ", max(l) - min(l))

# Q3 Solution:
l = [1,2,3,4,5,6,7,8,9,10] 
print("List: ",l)
print("Element inserted at 6th position which is 1/3rd of element at 4th position: ",end="")
l.insert(5, (l[3] * 1/3))
print(l)