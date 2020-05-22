import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    # stores number of tuples with two elements that can be formed if we find the key
    potential_two_tuples = defaultdict(int) 
    # stores number of tuples with three elements that can be formed if we find the key
    potential_three_tuples = defaultdict(int)
    count = 0
    for k in arr:
        # k completes the three tuples given we have already found k/(r^2) and k/r  
        count += potential_three_tuples[k]
        # For any element of array we can form three element tuples if we find k*r given k / r is already found. Also k forms the second element.
        potential_three_tuples[k*r] += potential_two_tuples[k]
        # For any element of array we can form two element tuples if we find k*r. Also k forms the first element.
        potential_two_tuples[k*r] += 1 
    return count

if __name__ == '__main__':
    n = 4

    r = 3

    arr = [1, 3, 9, 9, 27, 81]

    ans = countTriplets(arr, r)

    print(ans)
