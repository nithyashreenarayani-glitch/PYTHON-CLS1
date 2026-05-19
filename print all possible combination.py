from itertools import permutations

# Input list
numbers = [1, 2, 3]

# Generate all permutations
perms = permutations(numbers)

# Print each permutation
for p in perms:
    print(*p)