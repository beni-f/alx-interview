#!/usr/bin/python3
"""
    Minimum Operations
"""
def minOperations(n):
    operations = 1
    count = 0
    while(operations * 2 < n):
        count += 1
        operations *= 2
    if(operations * 2 == n):
        count += 1
    else:
        while(operations != n):
            count += 1 
            operations += 1
    return count

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))    