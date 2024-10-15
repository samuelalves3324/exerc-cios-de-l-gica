import math
import os
import random
import re
import sys

def staircase(n):

  for i in range(n):
    spaces = ""
    for j in range(n - (i + 1)):
       spaces += " "
    hashtags = ""
    for k in range(i + 1):
       hashtags += "#"
    print(spaces + hashtags)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
