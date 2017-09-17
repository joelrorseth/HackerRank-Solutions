#
# Merge the Tools
# Split a string into equal parts of size k, then modify each part to
# remove any subsequent occurrences of duplicate characters.
#

from collections import OrderedDict

def merge_the_tools(string, k):

    # Create list of substrings (taken in order) each of size k
    ksplit = lambda s, n: [s[i:i+k] for i in range(0, len(string), k)]

    # Remove subsequent duplicate characters in a string
    remove_dups = lambda s: "".join(OrderedDict.fromkeys(s))

    # Create new list by removing duplicate chars in split input
    split = ksplit(string, k)
    ans = [remove_dups(s) for s in split]

    for s in ans: print(s)


print("AABCAAADA")
merge_the_tools("AABCAAADA", 3)
