#!/bin/python3
#
# Left Rotation
# Perform left rotation on a list. Ex. a = [1,2,3,4,5] and d=3,
# output = [4,5,1,2,3]
#

import sys

def leftRotation(a, d):
    # Avoid unneccessary shifting
    d = d % len(a)
    
    # Slice leftmost 'd' elements, move to end of list
    return a[d:] + a[:d]

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = list(map(int, input().strip().split(' ')))
    result = leftRotation(a, d)
    print (" ".join(map(str, result)))
