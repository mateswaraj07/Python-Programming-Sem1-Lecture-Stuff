# 1. Index based for loop
a = [10,20,30,40,50,60]
print("Index based for loop")
for i in range(len(a)):
    if i % 2 == 0:
        print("Even Index Value: ",a[i])
#2. Value based for loop
print("Value based for loop")
for i in a:
    if i % 2 == 0:
        print("Even Value: ",i)
#3. Sum of all even values in list
l = [10,20,30,40,50,60]
sum = 0
for i in l:
    if i % 2 == 0:
        sum += i
print("List of values: ",l)
print("Sum of all even values in list: ",sum)

#with using steps. it reduces the number of iterations
print("Sum of all even values in list (using steps): ",sum)
sum = 0
for i in range(0, len(l), 2):
    sum += l[i]
print("Sum of all even values in list (using steps): ",sum)

# factorial of a number
n = 5
fact = 1
for i in range(1, n+1): #forward counting
    fact *= i
print("Factorial of", n, "is:", fact)
#backward counting factorial
fact = 1
for i in range(n, 0, -1): #backward counting
    fact *= i
print("Factorial of", n, "is:", fact)
#factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of", 5, "is:", factorial(5))

#leap year check
# leap year is a year in which February has 29 days. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400.
year = 2000
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): # 4 -> divisible by 4, 100 -> not divisible by 100, 400 -> divisible by 400
    print(year, "is a leap year")
