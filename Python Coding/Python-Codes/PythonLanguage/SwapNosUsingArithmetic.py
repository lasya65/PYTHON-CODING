#This is a program to swap two numbers without using a temp variable.
#Taking input from the user
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print(f"Before swapping x = {x} and y = {y}")
#Logic to swap two numbers
x = x + y
y = x - y
x = x - y
print(f"After swapping x = {x} and y = {y}")
