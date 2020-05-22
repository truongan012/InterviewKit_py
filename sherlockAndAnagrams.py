#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    sub_list = [''.join(sorted(s[i:j+1])) for i in range(len(s)) for j in range(i, len(s))]
    counter = Counter(sub_list)
    return sum((n*(n-1)//2) for n in counter.values())

if __name__ == '__main__':
    q = 1
    for q_itr in range(q):
        s = "abba"
        result = sherlockAndAnagrams(s)
        print(result)