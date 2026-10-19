# input two numbers and display division and remainder
def div_and_rem(x,y):
    div = x/y
    rem = x%y
    return f"Division= {div}, Remainder= {rem}"

x=int(input("Enter 1st Number: "))
y=int(input("Enter 2nd Number: "))
print(div_and_rem(x,y))