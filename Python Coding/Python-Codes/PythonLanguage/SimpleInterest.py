#This is a program to accept principal, rate of interest and time from the user and calculate simple interest.
#Taking input from the user 
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: ")) #Time is in years
#Calculating simple interest
simple_interest = (principal * rate * time) / 100
print(f"The simple interest is {simple_interest}") # Here f is used to format the string
