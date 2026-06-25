"""
Multiplication Table Generator
Author: Basavakiran

This program takes a number from the user and displays
its multiplication table from 1 to 10.
"""

# Get input from the user
number = int(input("Enter a number: "))

print(f"\nMultiplication Table of {number}\n")

# Generate multiplication table
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")