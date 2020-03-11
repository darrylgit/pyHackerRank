#!/bin/python3

import math
import os
import random
import re
import sys

from functools import reduce

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
  return reduce((lambda x, y : x + y), ar)