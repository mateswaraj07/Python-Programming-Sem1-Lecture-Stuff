# Accept sentence from user and count the vowels
sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count = 0
for char in sentence:
    if char in vowels:
        count += 1
print(f"Total vowels in the sentence: {count}")