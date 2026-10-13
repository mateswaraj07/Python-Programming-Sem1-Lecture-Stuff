# Take a sentence from the user, split it into words, and store them in a list. 
# Print longest word.
s = input("Enter a sentence: ")
words = s.split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest word:", longest)