#!/usr/bin//env python3

# Created by: maliksalem1
# Created on: October 2022
# This program compares two numbers


import random

def count_even(numbers):
    even_count = 0
    for number in numbers:
        if number % 2 == 0:
            even_count += 1
    return even_count

def main():
    random_numbers = random.sample(range(1, 51), 100)
    even_count = count_even(random_numbers)
    print("The list contains", even_count, "even numbers.")
    print("\nDone.")


if __name__ == "__main__":
    main()