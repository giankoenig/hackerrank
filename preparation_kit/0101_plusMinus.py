#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    sizeArr = len(arr)
    
    numPos = 0
    numNeg = 0
    numZer = 0
    
    ratioPos = 0
    ratioNeg = 0
    ratioZer = 0
    
    for x in arr:
        if x > 0:
            numPos += 1
        elif x < 0:
            numNeg += 1
        else:
            numZer += 1
    
    ratioPos = numPos/sizeArr
    ratioNeg = numNeg/sizeArr
    ratioZer = numZer/sizeArr     
    
    print("%6f" % ratioPos)
    print("%6f" % ratioNeg)
    print("%6f" % ratioZer)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)