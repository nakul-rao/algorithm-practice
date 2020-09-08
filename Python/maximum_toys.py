# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 13:26:13 2020

@author: Nakul Rao
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    print(prices)
    total_items = 0
    toy_set = []
    for i_idx, i in enumerate(prices):
        if total_items + prices[i_idx] > k:
            return len(toy_set)
        else:
            toy_set.append(i)
            total_items += i
            
if __name__ == '__main__':

    k = 7

    prices = [1,2,3,4]

    result = maximumToys(prices, k)

    print(result)