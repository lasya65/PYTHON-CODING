#This is a program which intakes binary code and converts it into a message
#The binary code is converted into ASCII code and then into a message
#The message is then printed out
#The program is run by calling the function binaryToMsg with the binary code as the argument
#The function returns the message
binary_input = " "
def binaryToMsg(binary_input):
    #Converting the binary code into ASCII code
    n = int(binary_input, 2)
    n = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    return n