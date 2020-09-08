# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 17:22:34 2020

@author: Nakul Rao
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    hour_glasses = []
    
    for i_idx, i in enumerate(arr):
        for j_idx, j in enumerate(i):
            try:
                if i_idx-1 < 0 or i_idx + 1 > len(arr)-1 or j_idx-1<0 or j_idx+1>len(i)-1:
                    raise ValueError("not an hour glass")
                hour_glass = []
                #top_3
                hour_glass.append(arr[i_idx-1][j_idx-1])
                hour_glass.append(arr[i_idx-1][j_idx])
                hour_glass.append(arr[i_idx-1][j_idx+1])
                #mid_3
                # hour_glass.append(arr[i_idx][j_idx-1])
                hour_glass.append(arr[i_idx][j_idx])
                # hour_glass.append(arr[i_idx][j_idx+1])
                #bottom_3
                hour_glass.append(arr[i_idx+1][j_idx-1])
                hour_glass.append(arr[i_idx+1][j_idx])
                hour_glass.append(arr[i_idx+1][j_idx+1])
                hour_glasses.append(sum(hour_glass))
            except ValueError as err:
                print("not an hour glass")
                
    return max(hour_glasses)
        

if __name__ == '__main__':

    arr = [
        [0,6,-7,1,6,3],
        [-8,2,8,3,-2,7],
        [-3,3,-6,-3,0,-6],
        [5,0,5,-1,-5,2],
        [6,2,8,1,3,0],
        [8,5,0,4,-7,4]
    ]

    result = hourglassSum(arr)
    
    print(result)

