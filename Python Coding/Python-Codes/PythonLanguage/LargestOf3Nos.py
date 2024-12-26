#Program to accept 3 numbers and find out the largest and the second largest of the 3 numbers
# Accepting 3 numbers from user
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))
# Checking if x is greater than y and z
if x > y and x > z:
    print("The largest number is: ", x)
    if y > z:
        print("The second largest number is: ", y)
    else:
        print("The second largest number is: ", z)
# Checking if y is greater than x and z
elif y > x and y > z:
    print("The largest number is: ", y)
    if x > z:
        print("The second largest number is: ", x)
    else:
        print("The second largest number is: ", z)
# Checking if z is greater than x and y
else:
    print("The largest number is: ", z)
    if x > y:
        print("The second largest number is: ", x)
    else:
        print("The second largest number is: ", y)

        if x == y == z:
            print("All the numbers are equal")
        elif x == y:
                print("The first and second numbers are equal")