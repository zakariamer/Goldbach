# Author: Zakaria Merzougui and Grant Foody

import math
import matplotlib.pyplot as plt
import time

# Set range of numbers to check
max = 10_000

count_array = []

# Checks to see if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    # Check up to sqrt(n) since that's the biggest one factor can be
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Loop through all even numbers from 2 to max and finds all possible pairs of prime numbers that sum to that even number and increases the count of pairs for that even number
start = time.perf_counter() # Time the calculation
for even in range(2, max + 1, 2):
    count = 0
    for i in range(2, even // 2 + 1):
        if is_prime(i) and is_prime(even - i):
            count += 1
    count_array.append(count)

# Print time taken
elapsed = time.perf_counter() - start
print(f"Completed in {elapsed} seconds.")

# Write the even number, the count of prime pairs that sum to it, and then list all pairs
with open("Goldbach_Landscape_Results.txt", "w") as file:
    for even in range(2, max + 1, 2):
        count = count_array[(even // 2) - 1]
        file.write(f"{even}: {count} pairs")
        file.write("\n")
        for i in range(2, even // 2 + 1):
            if is_prime(i) and is_prime(even - i):
                file.write(f"  {i} + {even - i}\n")
        file.write("\n")

print("Goldbach_Landscape_Results.txt file created.")

# Graph the results using matplotlib bar graph and shows all even numbers labelled on the x-axis and the count of pairs of prime numbers that sum to that even number on the y-axis
plt.bar([i for i in range(2, max + 1, 2)], count_array)
plt.title("Number of Prime Pairs that Sum to Even Numbers")
plt.xlabel("Even Numbers")
plt.ylabel("Count of Prime Pairs")
plt.show()