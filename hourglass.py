#!/bin/python3
#
# 2D Array - DS
#
# You are given a 6x6 array of integers. Each matrix of this size can contain
# 16 hourglasses, defined as a set of indicies that form an hourglass shape in
# the matrix. Find the largest sum of all values contained in any hourglass.
#
#                      0 0 0 0 0
#   Ex. hourglass ->   0 1 1 1 0   sum = 7
#                      0 0 1 0 0
#                      0 1 1 1 0
#

import sys

# Matrix representing the grid A containing hourglasses
A = []

for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    A.append(arr_t)

max_sum = -9 * 7

# Loop thru each row and column
# Subtract 2 to account for hourclass width and height
for row in range(len(A) - 2):
    for col in range(len(A[row]) - 2):
        
        # Assign variables in hourglass shape (in matrix)
        tl = A[row][col]
        tc = A[row][col + 1]
        tr = A[row][col + 2]
        mc = A[row + 1][col + 1]
        bl = A[row + 2][col]
        bc = A[row + 2][col + 1]
        br = A[row + 2][col + 2]
        
        # Add up all hourglass values and check if sum beats current
        s = tl + tc + tr + mc + bl + bc + br
        max_sum = max(max_sum, s)

print(max_sum)
