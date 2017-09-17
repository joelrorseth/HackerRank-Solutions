#!/bin/python3
#
# Sherlock and the Valid String
#
# Sherlock considers a string s to be valid if either of the following conditions are satisfied:
# 1. All characters in s have the same exact frequency (occur the same number of times)
# 2. Deleting exactly 1 character from s will result in all characters having the same frequency
#

import sys
from collections import Counter

def isValid(s):
    counter = Counter(s)
    count_freqs = list(counter.values())
    
    # Map character frequencies to their frequency
    freq_map = Counter(count_freqs)
    
    if len(freq_map) == 1:
        return True
    
    if len(freq_map) == 2:
        # If two frequency counts, one must be 1 (only occured to one char)
        for v in list(freq_map.values()):
            if v == 1:
                return True

# If there were > 2 frequency counts, impossible to satisfy
return False


if isValid(input().strip()):
    print("YES")
else:
    print("NO")
