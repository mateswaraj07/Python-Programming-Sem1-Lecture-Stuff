def get_max(*num):
    if len(num)==0:
        return None
    max=num[0]
    for n in num:
        if n>max:
            max=n
    return max

print(get_max(3,12,32,9,21))
print(get_max('Arush', 'Payal', 'Zarina', 'Yogesh'))
print(get_max('shreepad', 'swaraj', 'om', 'pravin'))