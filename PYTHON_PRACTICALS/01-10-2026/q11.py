# Remove duplicated from the list without using set()
l = [1, 2, 3, 2, 4, 1, 5]
new = []
for i in l:
    if i not in new:
        new.append(i)
print(new)