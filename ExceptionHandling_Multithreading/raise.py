#raise
try:
    num=int(input("Enter a number: "))
    if num<0:
        raise ValueError("Negative numbers are not allowed.")
    print(100/num)
except ValueError as ve:
    print("Error:", ve)