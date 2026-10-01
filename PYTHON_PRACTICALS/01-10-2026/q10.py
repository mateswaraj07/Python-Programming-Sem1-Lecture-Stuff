# Print the following pattern
#    *
#   + +
#  * * *
# + + + +
n = 4                             
for i in range(1, n + 1):          # Outer loop: runs once for each row
    for j in range(n - i):         # Print spaces; spaces decrease in every row
        print(" ", end=" ")        
    if i % 2 == 1:                 # Check if row number is odd
        ch = " * "                  # Odd row use *
    else:                           # If row number is even
        ch = " + "                  # Even row use +
    for k in range(i):             # Print the character i times
        print(ch, end=" ")         # Print * or + without going to next line
    print()                        # Move to the next line