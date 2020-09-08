# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 14:59:56 2020

@author: Nakul Rao
"""

#!/bin/python3

import math
import os
import random
import re
import sys
import json
from collections import Counter

# Complete the countTriplets function below.
def countTriplets(arr, r):
    r2 = Counter()
    r3 = Counter()
    count = 0
    
    for v in arr:
        if v in r3:
            count += r3[v]
        
        if v in r2:
            r3[v*r] += r2[v]
        
        r2[v*r] += 1

    return count

if __name__ == '__main__':

    r = 3

    arr = [1,3,9,9,27,81]

    ans = countTriplets(arr, r)

    print(ans)