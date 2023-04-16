#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    
    
    newName = ""
    index = 0
    
    for i in range(0,len(s)):
        
        if s[i].isalpha() == True and s[i-1] == " " or s[i].isalpha() == True and i==0:
            s =  f"{s[:i]}{(s[i]).upper()}{s[i+1:]}"
        
    return s

if __name__ == '__main__':
    

    s = input()

    result = solve(s)
    print(result)
