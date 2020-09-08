# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 11:59:17 2020

@author: Nakul Rao
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    sorts = 0
    for i_idx, i in enumerate(a):
        for j_idx, j in enumerate(a[0:-1]):
            if (a[j_idx] > a[j_idx + 1]):
                a[j_idx], a[j_idx+1] = a[j_idx+1], a[j_idx]
                sorts += 1
    
    print(f"Array is sorted in {sorts} swaps")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

if __name__ == '__main__':
    n = 3

    # a = [1,2,3,4,5,6,7,8,9]
    a = [1,4,3,2,5,9,6,7,8]

    countSwaps(a)
    
