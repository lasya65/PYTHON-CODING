#This is a program which takes the message from the user and converts it into binary form.
input_string = input("Enter the message: ")
print("The binary form of the message is: ")
for char in input_string:
    print(format(ord(char), '08b'), end=' ')
print()
