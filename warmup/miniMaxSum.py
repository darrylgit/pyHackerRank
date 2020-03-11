#!/bin/python3

import math
import os
import random
import re
import sys

from functools import reduce

# Complete the miniMaxSum function below.
def miniMaxSum(arr):

  miniSum = reduce((lambda x, y : x + y), sorted(arr)[0 : len(arr) - 1])
  maxSum = reduce((lambda x, y : x + y), sorted(arr)[1 : len(arr)])

  print(miniSum, maxSum)