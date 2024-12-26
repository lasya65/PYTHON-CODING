import math
from collections import deque

def is_perfect_square(num):
    """Check if a number is a perfect square."""
    root = int(math.sqrt(num))
    return root * root == num

def minimum_jumps(points):
    n = len(points)
    # Queue for BFS (index, jumps)
    queue = deque([(0, 0)])
    visited = set()
    visited.add(0)

    while queue:
        index, jumps = queue.popleft()
        
        # If we reach the last point
        if index == n - 1:
            return jumps
        
        # Check all valid next jumps
        for next_index in range(index + 1, n):
            if next_index not in visited and is_perfect_square(abs(points[next_index] - points[index])):
                queue.append((next_index, jumps + 1))
                visited.add(next_index)
                
    return 1  # If no valid path exists

# Example usage
points1 = [1, 2, 3]
points2 = [1, 2, 4]

print(minimum_jumps(points1))  # Output: 2
print(minimum_jumps(points2))  # Output: 1
