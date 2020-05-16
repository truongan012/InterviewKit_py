#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    if set1.intersection(set2) == set():
        return "NO"
    else:
        return "YES"

if __name__ == '__main__':
    q = 2
    for q_itr in range(q):
        s1 = "hi"
        s2 = "world"
        result = twoStrings(s1, s2)
        print(result)
