#python3
# Quadratic Equation
# Have the user enter in the coefficients of a quadratic equation in the
# format: ax^2 + bx + c = 0 and calculate the solutions of the equation
# rounded to 2 decimal places. Use a try...except block to catch if there
# is no solution


""" Sample output:
Enter in the coefficients for a quadratic equation in the format:
  ax^2 + bx + c = 0
a:3
b:d
c:1
Those are not valid values for a, b or c
a:3
b:2
c:1
There are no real roots to the equation
a:2
b:-3
c:-6
The roots are 2.64 and -1.14
a:1
b:8
c:16
The roots are -4.0 and -4.0
"""
import os
os.system('cls')


print("Enter in the coefficients for a quadratic equation in the format:")
print("  ax^2 + bx + c = 0")

import math
 
sixseven = input("a => ")
highway = input("b => ")
driveway = input("c => ")

print(f"your equation is -> {sixseven}x^2 + {highway}x + {driveway}")

try:
  seven = float(sixseven)
  way = float(highway)
  drive = float(driveway)
except:
  print("invalid input from the user, please try again")
  exit()

try:
  MRBLUEYOUDIDITRIGHT = (-way + (math.sqrt((way)**2 - (4*seven*drive)))) / (2*seven)
  BUTHERECOMESMRNIGHT = (-way - (math.sqrt((way)**2 - (4*seven*drive)))) / (2*seven)
  HANDISONYOURSHOULDER = round(MRBLUEYOUDIDITRIGHT, 2)
  NEVERMIND = round(BUTHERECOMESMRNIGHT, 2)
  print(f"yor roots are {HANDISONYOURSHOULDER} and {NEVERMIND}")
except:
  print("there are no real roots to this equation")

