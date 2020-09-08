# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 15:12:10 2020

@author: Nakul Rao
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    
    unique_set = list(set(ar))
    for i in unique_set:
        pairs += (ar.count(i) // 2)
    
    return pairs
    

if __name__ == '__main__':
    
    n = int("9")

    ar = [10,20,20,10,10,30,50,10,20]
    
    result = sockMerchant(n, ar)
    
    print(result)