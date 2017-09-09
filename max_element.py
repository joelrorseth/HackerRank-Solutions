#!/bin/python3
#
# Maximum Element
# Manage input queries controlling a stack with the following operations:
#
#   1 x  -Push the element x into the stack.
#   2    -Delete the element present at the top of the stack.
#   3    -Print the maximum element in the stack.
#

n = int(input())
stack = []

for i in range(n):
    line = input().split()
    query = line[0]

    # Push onto stack
    if query == '1':
        val = int(line[1])
        if len(stack) == 0:
            stack.append(val)
        else:
            # Push copies of max if smaller than current max
            # This is bc subsequent pops will yield same max anyway
            curr_max = stack[-1]
            stack.append(val if val > curr_max else curr_max)

    # Pop from stack
    elif query == '2':
        stack.pop()

    # Print max
    else:
        print(stack[-1])
