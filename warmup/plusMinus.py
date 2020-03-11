#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
  tracker = {
    "positives": 0,
    "negatives": 0,
    "zeroes": 0
  }

  length = len(arr)

  for i in range(length):
    if arr[i] > 0:
      tracker["positives"] += 1
    elif arr[i] < 0:
      tracker["negatives"] += 1
    else:
      tracker["zeroes"] += 1
  
  
  print(tracker["positives"] / length)
  print(tracker["negatives"] / length) 
  print(tracker["zeroes"] / length)