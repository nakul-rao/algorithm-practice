# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 16:58:23 2020

@author: Nakul Rao
"""

def fizzBuzz(n):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
            
if __name__ == '__main__':
    n = 15

    fizzBuzz(n)