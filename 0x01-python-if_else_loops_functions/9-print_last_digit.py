#!/usr/bin/python3


def print_last_digit(number):
    """Prints the last digit of a no. and return it."""
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
