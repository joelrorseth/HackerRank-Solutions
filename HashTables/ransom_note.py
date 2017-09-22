#
# Ransom Note
#
# Given a magazine contains a bunch of words, determine if a
# kidnapper would be able to cut out every word required to
# write a random note.
#

from collections import Counter


# Solution 1: Subtract character count dictionaries
def ransom_note_easy(magazine, ransom):
    return Counter(ransom) - Counter(magazine) == {}


# Solution 2: Manually create dictionaries
def ransom_note(magazine, ransom):
    mag = {}
    
    # Create hashtable / dictionary of all words in magazine
    for m in magazine:
        if m in mag:
            mag[m] += 1
        else:
            mag[m] = 1

    # Check for all words to be in magazine hashtable
    for r in ransom:
        if not r in mag or mag[r] == 0:
            return False
        else:
            mag[r] -= 1

    return True


# Demonstration
m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)

if(answer):
    print("Yes")
else:
    print("No")
