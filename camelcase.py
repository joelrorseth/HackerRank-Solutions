#!/bin/python3
#
# CamelCase
# Given a sentence containing words separated only by acapitalized first
# letters, determine the number of words. The first word will never be capitalized.
# Ex. saveChangesInTheEditor --> 5
#

import sys

s = input().strip()

# Use generator expression to create 1s for uppers
uppers = sum(1 for c in s if c.isupper())

# Account for first word which is never capitalized
if (len(s) > 0):
    uppers += 1;

print(uppers)
