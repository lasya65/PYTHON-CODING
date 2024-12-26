# This is a program to demonstrate the use of if-elif-else statements in Python
# We are going to apply in determining if a person could vote or not based on their age.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
elif age> 0 |age< 18:  # elif is a short form of else if , used for multiple else if conditions
    print("You are not eligible to vote")
else:
        print("Invalid age")