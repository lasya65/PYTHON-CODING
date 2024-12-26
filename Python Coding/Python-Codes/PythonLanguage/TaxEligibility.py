# Program to accept name and salary, check if their salary is >3L and if they are eligible to pay tax
name = input("Enter your name: ")   # Accepting name from user
salary = float(input("Enter your salary: "))  # Accepting salary from user
if salary > 300000:  # Checking if salary is greater than 3L
    print("You are eligible to pay tax")
else:
    print("You are not eligible to pay tax")
