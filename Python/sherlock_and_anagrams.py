# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 14:01:26 2020

@author: Nakul Rao
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    strlen = len(s)
    anagrams = 0
    
    list_of_sets = []
    
    for j in range(1,strlen):
        for i in range(strlen):
            if len(s[i:i+j]) < j:
                break
            else:
                list_of_sets.append(s[i:i+j])
    
    # Sort List
    for i_idx, i in enumerate(list_of_sets):
        list_of_sets[i_idx] = "".join(sorted(list_of_sets[i_idx]))
    
    
    for i in range(len(list_of_sets)):
        for j in range(i+1, len(list_of_sets)):
            if list_of_sets[i] == list_of_sets[j]:
                anagrams += 1
            else:
                if len(list_of_sets[j]) > len(list_of_sets[i]):
                    break
    print(anagrams)
    
if __name__ == '__main__':
    s = "kkkk"
    sherlockAndAnagrams(s)
