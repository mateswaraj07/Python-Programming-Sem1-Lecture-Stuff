# suppose n= 1232144 count how many time digit  or its frequency using an array.
# output:
# 1 -> 2
# 2 -> 2
# 3 -> 1
# 4 -> 2

# n = 1232144 
# s = str(n)
# arr = []
# for d in s:
#     arr.append(int(d))
# print(arr)   
# freq = [0] * 10
# for d in arr:
#     freq[d] += 1   
# for i in range(10):
#     if freq[i] > 0:
#         print(f"{i} -> {freq[i]}")


def countFreq(n):
    freq=[0]*10
    while n!=0:
        last_digit=n%10
        freq[last_digit]+=1
        n//=10
    return freq

n=134654987139
res=countFreq(n)
for i in range(len(res)):
    print(f"{i} -> {res[i]}")













# Program to count frequency of digits in a number using an array
# Step 1: Take input number
# Step 2: Convert number into a list of digits
# str(n) converts number to string, then we iterate each character and convert back to int
# Step 2: Convert number into a list of digits
# First, convert the number into a string
# Then, create an empty list to store digits
# Traverse each character in the string
 # Convert character back to integer and append to list
# Now arr contains all digits of the number
# Step 3: Create a frequency array of size 10 (for digits 0–9)
# Initially all values are 0
# Step 4: Traverse the digit array and update frequency
# increment count at index equal to digit
# Step 5: Print only digits that appear (non-zero frequency)


# Function to count frequency of digits in a number
# def countFreq(n):
#     # Step 1: Create a frequency array of size 10 (for digits 0–9)
#     freq = [0] * 10

#     # Step 2: Loop until the number becomes 0
#     while n != 0:
#         # Extract the last digit using modulus
#         last_digit = n % 10

#         # Increment the frequency of that digit
#         freq[last_digit] += 1

#         # Remove the last digit using integer division
#         n //= 10

#     # Step 3: Return the frequency array
#     return freq


# # Main program
# n = 134654987139   # Input number
# res = countFreq(n) # Call function to get frequency array

# # Step 4: Print digit frequencies
# for i in range(len(res)):
#     print(f"{i} -> {res[i]}")
