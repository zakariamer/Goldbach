# Author: Zakaria Merzougui and Grant Foody

import math

# Set range of numbers to check
max = 100000

# Checks to see if a number is prime
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Loops through all even numbers from 2 to max
for i in range(2, max + 1):
    # Check if number is even
    if i % 2 == 0:
        # Check if number can be expressed as sum of two primes
        found = False
        for j in range(2, i):
            if is_prime(j) and is_prime(i - j):
                found = True
                break
        if not found:
            print(f"{i} cannot be expressed as the sum of two primes.")