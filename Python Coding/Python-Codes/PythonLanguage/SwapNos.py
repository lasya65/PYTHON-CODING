#Program to swap two numbers.
x = int(input("Enter the first number: "))    #Taking input from the user
y = int(input("Enter the second number: "))   #Taking input from the user
print(f"Before swapping x = {x} and y = {y}")
temp = x
x = y
y = temp
print(f"After swapping x = {x} and y = {y}")
#The above program is swapping two numbers using a temp variable.