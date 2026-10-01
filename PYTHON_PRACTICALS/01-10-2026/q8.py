# Print the following pattern
#    *
#   * *
#  * * *
# * * * *
n = 4                              # Number of rows

for i in range(1, n + 1):         # Outer loop: runs from 1 to 4 (for each row)

    for j in range(n - i):         # Print spaces: spaces decrease in each row
        print(" ", end=" ")        # Print a space without moving to the next line

    for k in range(i):             # Print stars: stars increase in each row
        print(" * ", end=" ")        # Print a star without moving to the next line

    print()                        # Move to the next line after each row