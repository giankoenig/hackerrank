#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    convertedTime = '0'
    HH = s[:2]
    AMPM = s[-2:]
    if AMPM == 'AM' and HH != '12':
        convertedTime = s[:-2]
    elif AMPM == 'AM' and HH == '12':
        convertedTime = '00' + s[2:-2]
    elif AMPM == 'PM' and HH == '12':
        convertedTime = '12' + s[2:-2]
    else:
        HH = int(HH) + 12
        convertedTime = str(HH)+s[2:-2]
    
    return convertedTime

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    
    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()