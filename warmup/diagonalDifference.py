#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
  firstDiagonalSum = 0
  secondDiagonalSum = 0

  for i in range(len(arr)):
    firstDiagonalSum += arr[i][i]
    arr.reverse()
    secondDiagonalSum += arr[i][i]
    arr.reverse()
  
  return abs(firstDiagonalSum - secondDiagonalSum)