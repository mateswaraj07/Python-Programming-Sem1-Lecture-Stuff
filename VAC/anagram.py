# Function to count frequency of digits in a number
def countFreq(n):
    freq = [0] * 10   # array for digits 0–9
    while n != 0:
        last_digit = n % 10       # extract last digit
        freq[last_digit] += 1     # increment frequency
        n //= 10                  # remove last digit
    return freq
# Function to check if two numbers are anagrams
def isNumberAnagram(num1, num2):
    # Step 1: Get frequency arrays for both numbers
    freq1 = countFreq(num1)
    freq2 = countFreq(num2)
    # Step 2: Compare frequency arrays
    return freq1 == freq2
# Main program
n1 = 134654987139
n2 = 987134654139   # rearranged digits of n1
if isNumberAnagram(n1, n2):
    print(f"{n1} and {n2} are number anagrams")
else:
    print(f"{n1} and {n2} are not number anagrams")

























#String anagram
# Function to check if two strings are anagrams
# def isAnagram(str1, str2):
#     # Step 1: Remove spaces and convert to lowercase
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()
#     # Step 2: Sort both strings
#     return sorted(str1) == sorted(str2)
# # Main program
# word1 = "listen"
# word2 = "silent"
# # Step 3: Check and print result
# if isAnagram(word1, word2):
#     print(f"{word1} and {word2} are anagrams")
# else:
#     print(f"{word1} and {word2} are not anagrams")

# Number Anagram
# # Function to check if two numbers are anagrams
# def isNumberAnagram(num1, num2):
#     # Step 1: Convert numbers to string
#     str1 = str(num1)
#     str2 = str(num2)
#     # Step 2: If lengths differ, they can't be anagrams
#     if len(str1) != len(str2):
#         return False
#     # Step 3: Count digit frequencies for both numbers
#     freq1 = [0] * 10
#     freq2 = [0] * 10
#     for d in str1:
#         freq1[int(d)] += 1
#     for d in str2:
#         freq2[int(d)] += 1
#     # Step 4: Compare frequency arrays
#     return freq1 == freq2
# # Main program
# n1 = 12345
# n2 = 54321
# if isNumberAnagram(n1, n2):
#     print(f"{n1} and {n2} are number anagrams")
# else:
#     print(f"{n1} and {n2} are not number anagrams")