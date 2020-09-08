# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 11:48:21 2020

@author: Nakul Rao
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    for i in range(d):
        first_element = a[0]
        a.pop(0)
        a.append(first_element)
    return a

if __name__ == '__main__':

    d = 4

    a = [1,2,3,4,5]

    result = rotLeft(a, d)
    
    print(result)
