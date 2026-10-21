# def get_max(*names):
#     if len(names)==0:
#         return None
#     max=names[0]
#     for n in names:
#         if len(names)>len(max):
#             max=names
#     return max

# print(get_max('Arush', 'Payal', 'Zarina', 'Shreepad Suryawanshi'))
# print(get_max('shreepad', 'swaraj vishal mate', 'om', 'pravin'))

def get_max(*names):
    if len(names) == 0:
        return None
    longest = names[0]
    for n in names:
        if len(n) > len(longest):
            longest = n
    return longest

print(get_max('Arush', 'Payal', 'Zarina', 'Shreepad Suryawanshi'))
print(get_max('shreepad', 'swaraj vishal mate', 'om', 'pravin'))
