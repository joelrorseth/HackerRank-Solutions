#!/bin/python3
#
# Pangrams
# Determine if a string is a pangram, which is defined as a string
# that contains every letter in the alphabet at least once.
#

from collections import Counter

# Remove whitespace and lowercase stdin
s = "".join(input().split()).lower()

# Create counter of each character
counter = Counter(s)

# Counter should have counted 26 different elements
if (len(list(counter)) == 26):
    print("pangram")
else:
    print("not pangram")
