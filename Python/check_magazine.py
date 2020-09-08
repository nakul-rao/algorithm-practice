# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 13:38:21 2020

@author: Nakul Rao
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine.sort()
    note.sort()
    for word in note:
        if word in magazine:
            magazine.pop(magazine.index(word))
        else:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':

    magazine = "give me one grand today night".split()

    note = "give one grand today".split()

    checkMagazine(magazine, note)