# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 18:50:20 2020

@author: Nakul Rao
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    counter = 0
    for i in range(len(q)):
        if q[i]-(i+1) > 2:
            print("Too Chaotic")
            return

        for j in range(max(0,q[i]-2),i):
            if q[j] > q[i]:
                counter+=1
    print(counter)

if __name__ == '__main__':
    
    q = [1,2,5,3,7,8,6,4]
    minimumBribes(q)
