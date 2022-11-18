#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    
    ar.sort()
    unique = []
    for x in ar:
        if x not in unique:
            unique.append(x)
    
    pairs = []
    for x in unique:
        pairs.append(math.floor(ar.count(x)/2))
        
    numberOfPairs = sum(pairs)
    return numberOfPairs
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
