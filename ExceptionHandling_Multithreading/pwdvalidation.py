#Password Validation
try:
    password = input("Enter a password:")
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")
    print("Password is valid.")
except ValueError as e:
    print("Error:", e)

#modifying the above code that it accepts characters only
try:
    password = input("Enter a password:")
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")
    if not password.isalpha():
        raise ValueError("Password must contain only alphabetic characters.")
    print("Password is valid.")
except ValueError as e:
    print("Error:", e)