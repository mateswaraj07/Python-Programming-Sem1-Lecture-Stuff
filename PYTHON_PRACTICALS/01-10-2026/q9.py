# Accept sentence from user and count each vowel
sentence = input("Enter a sentence: ")

a = 0
e = 0
i = 0
o = 0
u = 0

for char in sentence:
    if char == 'a' or char == 'A':
        a += 1
    elif char == 'e' or char == 'E':
        e += 1
    elif char == 'i' or char == 'I':
        i += 1
    elif char == 'o' or char == 'O':
        o += 1
    elif char == 'u' or char == 'U':
        u += 1

print("A:", a)
print("E:", e)
print("I:", i)
print("O:", o)
print("U:", u)