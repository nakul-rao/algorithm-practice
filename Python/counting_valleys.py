# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 15:50:15 2020

@author: Nakul Rao
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    travelling_array = [i for i in s]
    sea_level = 0
    road_travelled = 0
    valleys = 0
    for i in travelling_array:
        print(i)
        if i == "U":
            road_travelled += 1
        elif i == "D":
            road_travelled -= 1
        if road_travelled == sea_level and i == "U":
            valleys += 1
    return valleys

if __name__ == '__main__':

    n = 8

    s = "DUDDDUUDUU"

    result = countingValleys(n, s)

    print(result)