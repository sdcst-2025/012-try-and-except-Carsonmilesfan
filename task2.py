#!python3

# Reciprocal
# have the user enter numbers and determine the 
# reciprocal of each number as a decimal and print it.
# use the try/except to find any invalid values and display
# the error message

#sample output:
"""
Enter a number: 0
The reciprocal of 0 does not exist
Enter a number: 1
The reciprocal of 1 is 1.0
Enter a number: 2
The reciprocal of 2 is 0.5
Enter a number: 3
The reciprocal of 3 is 0.3333333333333333
Enter a number: 4
The reciprocal of 4 is 0.25
"""

fella = input("enter a number=> ")

try:
    fella = float(fella)
    nifella = 1 / fella
    print(f"the reciprocol of {fella} is {nifella}")
except:
    print("that number is wrong, you entered a BAD number")