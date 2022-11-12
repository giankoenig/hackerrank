import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    
    n = len(matrix)
    k = 0

    for i in range(n//2):
    	for j in range(n//2):
    			k += max(matrix[i][j], matrix[n-i-1][j], matrix[i][n-j-1], matrix[n-i-1][n-j-1])
    	return k

arr = [[1, 7, 3, 1],[3, 4, 2, 5], [1, 9, 4, 1], [1, 9, 4, 1]]

print(arr)
flippedMatrix = flippingMatrix(arr)
print(flippedMatrix)
