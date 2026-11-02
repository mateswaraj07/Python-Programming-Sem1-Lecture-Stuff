def greet_person(name):
    print("Hello ", name+"!")

def change_case(text):
    result=""
    for ch in text:
        if ch.isupper():
            result += ch.lower()
        elif ch.islower():
            result += ch.upper()
        else:
            result += ch
    return result
            