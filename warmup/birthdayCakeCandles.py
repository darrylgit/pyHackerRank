#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
  ar.sort(reverse = True)
  
  tallCandles = 1

  for i in range(1, len(ar)):
    if ar[i] < ar[i - 1]:
      break
    tallCandles += 1
  
  return tallCandles