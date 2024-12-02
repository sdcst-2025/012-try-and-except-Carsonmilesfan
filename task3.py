#!python 3

# Square root of a number

# Have the user enter in a number.  Use a try-except to see if the input
# is a valid number.  Determine the square root and use a try-except to
# catch exceptions if the number can not be square rooted
# note: Use the math.sqrt() function to determine a square root
# rather than number**(0.5) as we need to catch complex numbers as
# exceptions

"""
Sample Output
Enter a number:x
That is not a valid number
There is no square root   
Enter a number:-1
There is no square root
Enter a number:3       
The square root of 3.0 is 1.7320508075688772
"""
import math

sigma = input("enter a number =>")

try:
    beta = float(sigma)
    print("that is a valid number sir")
    try:
        alpha = math.sqrt(beta)
        print(f"the square root of {beta} is {alpha}")
    except:
        print("there is no valid square root sir")
except:
    print("that is not a valid number sir")
    print("there is no square root sir")
    

