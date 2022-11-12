#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    numberOfValleys = 0
    threshold = 0
    valley = False # set to 1 if threshold < 0, reset at threshold = 0
    for idx, i in enumerate(path):
        if i == 'D':
            threshold -= 1
        elif i == 'U':
            threshold += 1
        else:
            print('not a valid path')
            break
        if threshold < 0:
            valley = True
        elif threshold > 0:
            valley = False
        elif threshold == 0 and valley == True:
            numberOfValleys += 1
        else:
            continue     
    return numberOfValleys
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
