#nested try 
try:
    num=int(input("Enter a number"))
    try:
        result=100/num
    except ZeroDivisionError:
        print("Cannot Divide by Zero")
except ValueError:
    print("Invalid Input")