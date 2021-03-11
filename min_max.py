import math
import os
import random
import re
import sys

# Complete the riddle function below.
def riddle(arr):
    # complete this function
    _size = len(arr)
    lst = []
    for i in range(_size):
        lst.append(max(arr))
        arr.remove(max(arr))
    return lst
    

if __name__ == '__main__':

    arr = [2,6,1,12]
    res = riddle(arr)
    print(res)