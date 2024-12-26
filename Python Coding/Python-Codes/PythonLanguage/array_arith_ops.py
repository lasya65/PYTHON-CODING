# Define the arrays
array1 = [1, 2, 3, 4, 5]  # First 5 natural numbers
array2 = [2, 3, 5, 7, 11]  # First 5 prime numbers

# Perform arithmetic operations
addition = [a + b for a, b in zip(array1, array2)]
subtraction = [a - b for a, b in zip(array1, array2)]
multiplication = [a * b for a, b in zip(array1, array2)]
division = [a / b for a, b in zip(array1, array2)]

# Print the results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)