# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:47:02 2020

@author: Nakul Rao
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    s_len = len(s)
    whole_string = s_len * (n // s_len)
    remainder_string = n - whole_string
    total_occurances_single = s.count('a')
    whole_string_occurance = total_occurances_single * (n // s_len)
    partial_string_occurance = s[0:remainder_string].count('a')
    total_occurance = whole_string_occurance + partial_string_occurance
    return total_occurance

if __name__ == '__main__':

    s = 'a'

    n = 100000000000

    result = repeatedString(s, n)

    print(result)
