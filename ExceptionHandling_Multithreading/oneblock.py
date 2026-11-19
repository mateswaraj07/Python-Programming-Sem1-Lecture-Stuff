#one block for multiple exceptions
try:
    num=int(input("Enter a number: "))
    print(100/num)
except (ValueError, ZeroDivisionError):
    print("Invalid input or cannot divide by zero. Please enter a valid non-zero number.")