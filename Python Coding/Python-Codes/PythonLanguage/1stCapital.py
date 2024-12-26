def change_case(test_cases):
    results = []
    for s in test_cases:
        if s[0].isupper():
            results.append(s.upper())
        else:
            results.append(s.lower())
    return results

# Input
T = int(input())  # Number of test cases
test_cases = [input().strip() for _ in range(T)]

# Processing
results = change_case(test_cases)

# Output
for result in results:
    print(result)
