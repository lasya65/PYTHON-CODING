#This is a program to calculate the sum of the first n cubes, where n is a user input.
n=int(input())
sum=0
for i in range(1,n+1):
    sum+=i**3
print(sum)
