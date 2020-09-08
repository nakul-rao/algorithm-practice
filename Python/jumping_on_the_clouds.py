# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:12:25 2020

@author: Nakul Rao
"""

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    shortest_distance = 0
    current_position = 0
    course_length = len(c) - 1
    
    while current_position < course_length:
        if current_position+2 <= course_length:
            if c[current_position+2] == 0:
                current_position = current_position + 2
            else:
                current_position = current_position + 1
        else:
            current_position = current_position + 1        
        shortest_distance += 1
    
    return shortest_distance

if __name__ == '__main__':
    
    n = 7

    c = [0,0,1,0,0,1,0]
    
    result = jumpingOnClouds(c)

    result = jumpingOnClouds(c)

    print(result)