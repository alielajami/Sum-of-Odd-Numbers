n = int(input("Enter a number: "))

# Store the sum of odd numbers
sum_of_odds = 0

# Iterate through all numbers from 1 to n
for i in range(1, n + 1):
    # Check if the current number is odd
    if i % 2 != 0:
        # Add it to the sum
        sum_of_odds += i

print("Sum of all odd numbers up to", n, "is:", sum_of_odds)