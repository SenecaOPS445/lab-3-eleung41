#!/usr/bin/env python3
'''Lab 3 Part 1 script - functions'''
# Author ID: 147724231

def sum_numbers(number1, number2):
    # Returns the sum of two numbers
    return int(number1) + int(number2)

def subtract_numbers(number1, number2):
    # Returns the difference between two numbers
    return int(number1) - int(number2)

def multiply_numbers(number1, number2):
    # Returns the product of two numbers
    return int(number1) * int(number2)

if __name__ == '__main__':
    print(sum_numbers(10, 5))      # Expected output: 15
    print(subtract_numbers(10, 5)) # Expected output: 5
    print(multiply_numbers(10, 5)) # Expected output: 50

