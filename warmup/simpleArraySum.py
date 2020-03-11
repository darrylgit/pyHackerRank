#!/bin/python3

import os
import sys
from functools import reduce
#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    return reduce((lambda x, y : x + y), ar)