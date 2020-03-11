#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
  aliceScore = 0
  bobScore = 0
  
  for i in range(len(a)):
    if a[i] > b[i]:
      aliceScore += 1
    elif a[i] < b[i]:
      bobScore += 1
    
  return [aliceScore, bobScore]