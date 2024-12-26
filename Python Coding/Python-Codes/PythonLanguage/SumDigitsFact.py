# This is a program to calculate the sum of the digits of factorial of a number using str
n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
fact_str = str(fact)
sum_digits = sum(int(digit) for digit in fact_str)
print(sum_digits)