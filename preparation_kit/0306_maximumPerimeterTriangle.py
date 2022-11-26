#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here
    sticks.sort()
    
    _triangles = []
    _triangle = []
    _solutions = []
    solution = []

    for ida, a in enumerate(sticks):
        for idb, b in enumerate(sticks[ida+1:]):
            for idc, c in enumerate(sticks[ida+1+idb+1:]):
                if a + b > c:
                    _triangle.append(a)
                    _triangle.append(b)
                    _triangle.append(c)
                    _triangles.append(_triangle)
                    _triangle = []
            

# [[2, 3, 4], [2, 4, 5], [3, 4, 5]]

    if _triangles != []:
        # loop through all valid triangles and find the one with maximum perimeter
        solution = (_triangles[-1][0], _triangles[-1][1], _triangles[-1][2])
        # if two have same perimeter, find the one with maximum length
        # if two have same maximum side, find the one with maximum minimum length
    else:
        solution.append(-1)
            
    return solution

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
