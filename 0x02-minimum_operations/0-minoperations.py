#!/usr/bin/python3
"""
    Minimum Operations
"""


def minOperations(n):
    operations = 1
    count = 0
    while (operations * 2 < n):
        count += 1
        operations *= 2
    if (operations * 2 == n):
        count += 1
    else:
        while (operations != n):
            count += 1
            operations += 1
    return count
