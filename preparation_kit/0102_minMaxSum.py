#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    totalSum = sum(arr)
    minSum = totalSum-max(arr)
    maxSum = totalSum-min(arr)
    
    print(minSum, maxSum)
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
