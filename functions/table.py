# w.a.f to input a number and display the table of the number
def table(num):
    for i in range(1,11):
        print(f"{num} * {i} = {num*i}")

num=int(input("Enter a Number: "))
table(num)