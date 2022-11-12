#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    isPangram = []
    slower = s.lower()

    checkArray = 'abcdefghijklmnopqrstuvwxyz '
    
    for l in checkArray:
        print(l)
        if l in slower:
            isPangram.append(True)
        else:
            isPangram.append(False)
    
    if all(isPangram):
        return 'pangram'
    else:
        return 'not pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
