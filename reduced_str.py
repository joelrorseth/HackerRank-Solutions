#!/bin/python3
#
# Super Reduced String
# Given a string, remove all consecutive identical characters.
#

import sys

def super_reduced_string(s):
    # Use stack / list to track last seen letter
    stack = []
    for c in s:
        # Push if not seen prev
        if (not stack or stack[-1] != c):
            stack += c
        # Pop if seen prev
        else:
            stack.pop()
    if stack:
        return ''.join(stack)
    else:
        return "Empty String"

s = input().strip()
result = super_reduced_string(s)
print(result)
