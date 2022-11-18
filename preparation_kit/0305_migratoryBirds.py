#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    
    arr.sort()
    unique = []
    countType = []
    indexMostFrequentType = 0
    mostFrequentType = 0
    
    for x in arr:
        if x not in unique:
            unique.append(x)
            
    for x in unique:
        countType.append(arr.count(x))
    
    indexMostFrequentType = countType.index(max(countType))
    mostFrequentType = unique[indexMostFrequentType]
    
    maxType = mostFrequentType
    return maxType
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
