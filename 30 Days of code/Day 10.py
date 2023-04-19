#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    binaryNum = bin(n).replace("0b", "")
    
    consecutiveList = []
    consecutiveOne = 0
    for index in range(len(binaryNum)):
        if binaryNum[index] == "1" :
            consecutiveOne += 1
            while True:
                try: 
                    if binaryNum[index+1] == "1":
                        consecutiveOne += 1
                        index += 1
                    else:
                        consecutiveList.append(consecutiveOne)
                        consecutiveOne = 0
                        break
                except IndexError:
                        consecutiveList.append(consecutiveOne)
                        consecutiveOne = 0
                        break
                        
    consecutiveList.sort()
    print(consecutiveList[-1])
    
                