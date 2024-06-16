#!/usr/bin/python3
"""
    Minimum Operations
"""


def minOperations(n):
    if (n <= 0):
        return 0

    operations = 0
    iterator = 2
    while (iterator <= n):
        if (n % iterator == 0):
            n = int(n / iterator)
            operations += iterator
            iterator = 1
        iterator += 1
    return operations
