# This is a program to take two binary strings with length N and choose any pairs of integers (i,j) such that 1<=i<=j<=N
# and swap the ith and jth character of S
# The first line of input contains a single integer T denoting the number of test cases.
# For each test case, input N, S, and R respectively.
# Output: For each test case, print a single line containing the string "YES" if it is possible to change S to R or "NO" if it is impossible (without quotes)

def can_transform(s1, s2):
    return sorted(s1) == sorted(s2)

T = int(input("Enter number of test cases: "))
for _ in range(T):
    n = int(input("Enter the length of the binary strings: "))
    s1 = input("Enter the first binary string: ")
    s2 = input("Enter the second binary string: ")
    if can_transform(s1, s2):
        print("YES")
    else:
        print("NO")