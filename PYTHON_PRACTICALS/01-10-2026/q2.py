# Accept two values S and N. Print square of first N numbers starting from S.
S = int(input("Enter Starting Value: "))
N = int(input("Enter Ending Value: "))
print(f"Square of numbers form {S} to {N}: ")
for i in range(S,N+1):
    print(f"{i} = {i*i}")
