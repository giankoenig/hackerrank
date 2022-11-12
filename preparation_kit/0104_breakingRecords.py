#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    minScore = 0
    minCount = 0
    maxScore = 0
    maxCount = 0
    
    for i, score in enumerate(scores):
        if i == 0:
            minScore = score
            maxScore = score
        if score < minScore:
            minScore = score
            minCount += 1
        if score > maxScore:
            maxScore = score
            maxCount += 1
    
    return maxCount, minCount
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
