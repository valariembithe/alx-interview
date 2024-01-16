#!/usr/bin/env python3
""" Task 0 module"""


def minOperations(n: int) -> int:
    """ Returns min no of operations"""
    if (n <= 0):
        return 0
    if not isinstance(n, int):
        return 0
    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
