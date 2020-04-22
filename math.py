# This is Noam's first program. It does math

# so the computer knows that it is the right number
valid = True

# Pick the math choice
choice = input("""
______________________________
What kind of math do you want?|
1 for addition                |
2 for subtraction             |
3 for multiplication          |
4 for division                |
______________________________
""")
if choice != 1 and choice != 2 and choice != 3 and choice != 4:
  print("You can not do this number only 1,2,3,4")
  valid = False

if valid == True:  
  # Get the x input
  x = float(input("what is the first number: "))

  # Get the y input
  y = float(input("What is second number: "))

  # Determine what to do with x and y
  if choice == 1:
    print("X + Y = " + str(x + y))
  if choice == 2:
    print("X - Y = " + str(x - y))
  if choice == 3:
    print("X * Y = " + str(x * y))
  if choice == 4:
    print("X / Y = " + str(x / y))





### How to improve:
# 1. error-check : the only input allowed is a number
# 2. give user option to choose which math to do
# 3. user interface
# 4. Colors
####