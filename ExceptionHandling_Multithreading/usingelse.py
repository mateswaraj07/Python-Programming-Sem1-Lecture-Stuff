#using else block
try:
    num=int(input("Enter a number: "))
    print(100/num)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero. Please enter a non-zero number.")
else:
    print("The operation was successful. The result is:", 100/num)