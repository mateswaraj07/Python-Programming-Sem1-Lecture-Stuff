#demonstrate finally block
try:
    print("Processing Transaction...")
    amount = int(input("Enter the amount to withdraw: "))
    if amount > 1000:
        print("Transaction approved.")
except:
    print("Transaction failed.")
finally:
    print("Thank you for using our banking services. Have a great day!")