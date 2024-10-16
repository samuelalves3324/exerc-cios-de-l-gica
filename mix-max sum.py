import math
import os
import random
import re
import sys

def miniMaxSum(arr: list):
    maxSum = 0
    minSum = 0

    for i in range(len(arr)):
        arryCopy = arr.copy()
        arryCopy.pop(i)
        sum = 0
        for j in arryCopy:
            sum += j
        if i == 0:
            maxSum = sum
            minSum = sum
        elif sum > maxSum:
            maxSum = sum
        elif sum < minSum:
            minSum = sum
    
    print(minSum, maxSum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
